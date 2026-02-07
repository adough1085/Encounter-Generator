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

class Location(BaseModel):
    name: str

class Locations(BaseModel):
    pkmn_name: str
    locations: List[Location]

def pkmn_to_str(pkmn: Pokemon):
    return pkmn.name

def convert_box(box: Pokemons):
    list = []
    for pkmn in box:
        list.append(pkmn_to_str(pkmn))
    return list

def str_to_location(location: str):
    return Location(name=location)

def convert_locations(old_locations: List[str]):
    new_list = []
    for old_location in old_locations:
        new_list.append(str_to_location(old_location))
    return new_list


app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
                   )

memory = {"s1" : []}

@app.get("/pokemons", response_model=Pokemons)
def get_pokemons():
    return Pokemons(pokemons=memory["s1"])

@app.post("/pokemons", response_model=Pokemon)
def add_pokemon(pokemon: Pokemon):
    memory["s1"].append(pokemon)
    return pokemon

@app.post("/locate", response_model=Locations)
def locate_pokemon(pokemon: Pokemon):
    g = Game("Scarlet")
    g.box = convert_box(memory["s1"])
    habitats = g.locate(pokemon.name, False)
    return Locations(pkmn_name=pokemon.name, locations=convert_locations(habitats))
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
g = Game("Scarlet")
g.box = ["Crocalor","Clodsire","Gumshoos","Arrokuda","Klawf","Bombirdier", "Magikarp", "Gimmighoul","Azumarill","Oinkologne (Male)","Tauros (Combat Breed)", "Goomy","Basculin (Red-Striped)"]
g.print_box()
#g.load_box_string("Crocalor,Clodsire,Gumshoos,Arrokuda,Klawf,Bombirdier,Magikarp,Gimmighoul,Azumarill,Oinkologne (Male),Tauros (Combat Breed),Goomy,Basculin (Red-Striped),")
g.populate_dupes()
g.distribution("Great Crater of Paldea","Day","Flying",0,True)
g.generate("Great Crater of Paldea",1,"Flying",0,True)
#g.generate(8,1,"Flying",0)
#g.distribution(9,1,"Normal",0)
#g.generate(15,1,"Fairy",1)
g.locate("misdreavus", True)
"""