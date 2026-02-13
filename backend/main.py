import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from models.game import Game as Game

class Pokemon(BaseModel):
    name: str

class Pokemons(BaseModel):
    pokemons: List[Pokemon]

def pkmn_to_str(pkmn: Pokemon):
    return pkmn.name

def convert_pkmns_to_str(pkmns: Pokemons):
    list = []
    for pkmn in pkmns:
        list.append(pkmn_to_str(pkmn))
    return list

class Location(BaseModel):
    name: str

class Locations(BaseModel):
    pkmn_name: str
    locations: List[Location]

def str_to_location(location: str):
    return Location(name=location)

def convert_locations(old_locations: List[str]):
    new_list = []
    for old_location in old_locations:
        new_list.append(str_to_location(old_location))
    return new_list

class Distribution_Input(BaseModel):
    game: str
    area: str
    time: str
    pkmnType: str
    power: str
    dupes: str
    sharedText: str
    specificPkmn: bool

class Distribution(BaseModel):
    pkmn_name: str
    percentage: float

class Distributions(BaseModel):
    location_name: str
    distributions: List[Distribution]

def str_to_distribution(pkmn_name: str, percentage: float):
    return Distribution(pkmn_name=pkmn_name, percentage=percentage)

def convert_distributions(old_distributions: List):
    new_list = []
    for pkmn in old_distributions: # pkmn instances have attributes name, percentage, and truncated_percentage
        pkmn_name = pkmn.name.split("_")[0]
        percent = pkmn.truncated_percentage
        new_list.append(str_to_distribution(pkmn_name, percent))
    return new_list

class Generation_Input(BaseModel):
    game: str
    area: str
    time: str
    pkmnType: str
    power: str
    dupes: str
    sharedText: str
    specificPkmn: bool

class Generation_Output(BaseModel):
    area: str
    time: str
    pkmn_name: str

class Test_Model(BaseModel):
    string: str

def convert_generation(old_generation: List):
    return Generation_Output(area=old_generation[0],time=old_generation[1],pkmn_name=old_generation[2])


app = FastAPI()

origins = [
    "https://localhost:5173", # origin for testing 
    "https://3.137.101.123" # origin for deployment
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
                   )


game_file = ""
base_scarlet = Game("Scarlet") # Held in server memory such that games are not recompiled every request, only copied
base_violet = Game("Violet")   # Held in server memory such that games are not recompiled every request, only copied
memory = {"s1" : [Pokemon(name="Bulbasaur")]}

@app.get("/", response_model=Pokemons)
def get_pokemons():
    empty_pkmns = [Pokemon(name="Placeholder")]
    return Pokemons(pokemons=empty_pkmns)

@app.post("/generate", response_model=Generation_Output)
def generate(gen_input: Generation_Input):
    g = Game(gen_input.game)
    generated_pkmn = g.process_generate_distribution_request("generate",gen_input.sharedText, gen_input.area, gen_input.time, gen_input.pkmnType, int(gen_input.power), gen_input.dupes, gen_input.specificPkmn, False)
    return convert_generation(generated_pkmn)

@app.post("/distribution", response_model=Distributions)
def distribution(dist_input: Distribution_Input):
    g = Game(dist_input.game)
    calculated_dist = g.process_generate_distribution_request("distribution",dist_input.sharedText, dist_input.area, dist_input.time, dist_input.pkmnType, int(dist_input.power), dist_input.dupes, dist_input.specificPkmn, False)
    return Distributions(location_name=dist_input.area, distributions=convert_distributions(calculated_dist))


@app.post("/locate", response_model=Locations)
def locate_pokemon(pokemon: Pokemon):
    g = Game("Scarlet") # Does not check for dupes or version exclusives, just need this to initialize a game
    habitats = g.locate(pokemon.name, False) # habitats[last index] = Pokémon name
    
    real_pkmn_name = pokemon.name.title()
    if any(habitats): # If a location was found...
        real_pkmn_name = Game.remove_version_exclusive_tag(real_pkmn_name)
        real_pkmn_name = Game.add_version_exclusive_tag(real_pkmn_name)

    return Locations(pkmn_name=real_pkmn_name, locations=convert_locations(habitats))

"""
Testing
    Run backend with ./main.py
    Run frontend with npm run dev
Production
    Run backend with python .\main.py
    Deploy frontend with npm run build
"""
# sample change

if __name__ == "__main__":
    uvicorn.run(app,
                #"main:app",
                host="0.0.0.0",
                port=8000,
                proxy_headers=True, 
                forwarded_allow_ips="*"
                )