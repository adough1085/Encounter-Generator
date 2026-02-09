import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from models.game import Game as Game
from modules import v as Validator

class Pokemon(BaseModel):
    name: str

class Pokemons(BaseModel):
    pokemons: List[Pokemon]

def pkmn_to_str(pkmn: Pokemon):
    return pkmn.name

def filter_request_str(string: str):
    pkmn_list = string.split(",")
    pkmn_list = list(map(lambda x: x.strip(), pkmn_list))
    pkmn_list = list(map(lambda x: add_exclusive_tag(x) if real_pokemon(x) else False, pkmn_list)) # Checks Pokemon name, filters out fake names, add tag if applicable
    pkmn_list = [pkmn for pkmn in pkmn_list if pkmn] # Filters out False
    return pkmn_list

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
    for pkmn in old_distributions:
        pkmn_name = pkmn.name.split("_")[0]
        percent = pkmn.percentage
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

class Generation_Output(BaseModel):
    area: str
    time: str
    pkmn_name: str

class Test_Model(BaseModel):
    string: str

def convert_generation(old_generation: List):
    return Generation_Output(area=old_generation[0],time=old_generation[1],pkmn_name=old_generation[2])

def real_pokemon(string):
    return Validator.valid_pokemon(string)

def add_exclusive_tag(string):
    status = Validator.version_exclusive(string)
    if status == "scarlet":
        string = f"{string.strip().title()} (Scarlet)"
    elif status == "violet":
        string = f"{string.strip().title()} (Violet)"
    return string.strip().title()

def distinguish_game(string_of_game):
    string_of_game = string_of_game.strip().lower()
    if string_of_game == "scarlet":
        return base_scarlet
    elif string_of_game == "violet":
        return base_violet

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
    g = distinguish_game(gen_input.game)
    g.box = filter_request_str(gen_input.sharedText)

    dupes = True if gen_input.dupes == "Yes" else False
    if dupes:
        g.populate_dupes()

    area = gen_input.area
    time = gen_input.time
    pkmnType = gen_input.pkmnType
    power = int(gen_input.power)
    generated_pkmn = g.generate(area, time, pkmnType, power, dupes, True)
    return convert_generation(generated_pkmn)

@app.post("/distribution", response_model=Distributions)
def distribution(dist_input: Distribution_Input):
    g = distinguish_game(dist_input.game)
    g.box = filter_request_str(dist_input.sharedText)
    for x in g.box:
        print(x)

    dupes = True if dist_input.dupes == "Yes" else False
    if dupes:
        g.populate_dupes()
    
    area = dist_input.area
    time = dist_input.time
    pkmnType = dist_input.pkmnType
    power = int(dist_input.power)
    calculated_dist = g.distribution(area, time, pkmnType, power, dupes, True)
    return Distributions(location_name=area, distributions=convert_distributions(calculated_dist))


@app.post("/locate", response_model=Locations)
def locate_pokemon(pokemon: Pokemon):
    g = distinguish_game("Scarlet") # Does not check for dupes 
    #g.box = convert_pkmns_to_str(memory["s1"])
    habitats = g.locate(pokemon.name, False)
    return Locations(pkmn_name=pokemon.name.title(), locations=convert_locations(habitats))

"""
Testing
    Run backend with ./main.py
    Run frontend with npm run dev
Production
    Run backend with python .\main.py
    Deploy frontend with npm run build
"""

if __name__ == "__main__":
    uvicorn.run(app,
                #"main:app",
                host="0.0.0.0",
                port=8000,
                proxy_headers=True, 
                forwarded_allow_ips="*"
                )