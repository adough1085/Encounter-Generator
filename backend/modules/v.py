import random

def correct_version(game_string, pkmn_to_check):
        """
        Docstring for correct_version
        
        :param self: Area object.
        :param game_string: String object representing game version, either "Scarlet" or "Violet"
        :param pkmn_to_check: String object representing name of Pokemon.
        """
        if game_string.lower() == "scarlet" and pkmn_to_check.lower().find("violet") == -1:
            return True
        elif game_string.lower() == "violet" and pkmn_to_check.lower().find("scarlet") == -1:
            return True 
        else:
            return False

def power(power_int):
        """
        Docstring for power_int
        
        :param self: Area object.
        :param power_int: An Integer intended to 1, 2, or 3. Depending on power_int level, it has a greater chance of forcing a specific Type (Grass, Water, etc.) Pokemon to spawn.
        
        upper_bound represents the percentage chance that a specific Type Pokemon is forced to spawn.
        Generates a random number from 1 to 100 (inclusive), if it is less than or equal to the upper_bound, then the specific Type is forced.
        """
        upper_bound = 0
        if power_int == 1:
            upper_bound = 50
        elif power_int == 2:
            upper_bound = 75
        elif power_int == 3: 
            upper_bound = 100
        else:
            return False
        
        if random.randint(1,100) <= upper_bound:
            return True
        else:
            return False

def valid_area(string_input):
        areas = {
        "Alfornada Cavern",
        "Asado Desert",
        "Cabo Poco",
        "Casseroya Lake",
        "Dalizapa Passage",
        "East Paldean Sea",
        "East Province (Area One)",
        "East Province (Area Two)",
        "East Province (Area Three)",
        "Glaseado Mountain",
        "Great Crater of Paldea",
        "Inlet Grotto",
        "North Paldean Sea",
        "North Province (Area One)",
        "North Province (Area Two)",
        "North Province (Area Three)",
        "Poco Path",
        "Pokemon League",
        "Socarrat Trail",
        "South Paldean Sea",
        "South Province (Area One)",
        "South Province (Area Two)",
        "South Province (Area Three)",
        "South Province (Area Four)",
        "South Province (Area Five)",
        "South Province (Area Six)",
        "Tagtree Thicket",
        "West Paldean Sea",
        "West Province (Area One)",
        "West Province (Area Two)",
        "West Province (Area Three)"
        }

        return any(string_input.lower() == area.lower() for area in areas)

def valid_type(string_input):
    types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
    string_input = string_input.strip().lower()
    return any(string_input.strip().lower() == pkmn_type.strip().lower() for pkmn_type in types)

def resolve_daypart(time):
        valid = True
        valid_dayparts = {"Dawn", "Day", "Dusk", "Night"}
        daypart = ""

        if isinstance(time, str):
            time = time.title()
            for dp in valid_dayparts:
                if time == dp:
                    daypart = dp
                    break

        if isinstance(time, int):
            if time == 0:
                daypart = "Dawn"
            elif time == 1:
                daypart = "Day"
            elif time == 2:
                daypart = "Dusk"
            elif time == 3:
                daypart = "Night"
            else:
                valid = False

        if valid == False:
            return False
        elif daypart != "":
            return daypart

def valid_pokemon(string_input):
    pokedex = set()
    with open(r"data/pokedex/paldea_dex.txt","r") as f1:
        temp = f1.readlines()
        for x in range(len(temp)):
            pokedex.add(temp[x][0:len(temp[x])-1].strip())
    return any(string_input.strip().lower() == pkmn.strip().lower() for pkmn in pokedex)

def version_exclusive(string_input):
    scarlet = set()
    violet = set()

    scarlet.add("Vulpix")
    scarlet.add("Ninetails")
    scarlet.add("Tauros (Blaze Breed)")
    scarlet.add("Gligar")
    scarlet.add("Larvitar")
    scarlet.add("Pupitar")
    scarlet.add("Tyranitar")
    scarlet.add("Cranidos")
    scarlet.add("Rampardos")
    scarlet.add("Drifloon")
    scarlet.add("Drifblim")
    scarlet.add("Stunky")
    scarlet.add("Skuntank")
    scarlet.add("Gliscor")
    scarlet.add("Deino")
    scarlet.add("Zweilous")
    scarlet.add("Hydreigon")
    scarlet.add("Skrelp")
    scarlet.add("Dragalge")
    scarlet.add("Oranguru")
    scarlet.add("Cramorant")
    scarlet.add("Stonjourner")
    scarlet.add("Armarouge")
    scarlet.add("Great Tusk")
    scarlet.add("Scream Tail")
    scarlet.add("Brute Bonnet")
    scarlet.add("Flutter Mane")
    scarlet.add("Slither Wing")
    scarlet.add("Sandy Shocks")
    scarlet.add("Roaring Moon")
    scarlet.add("Koraidon")
    scarlet.add("Walking Wake")
    scarlet.add("Gouging Fire")
    scarlet.add("Raging Bolt")

    violet.add("Sandshrew")
    violet.add("Sandslash")
    violet.add("Tauros (Aqua Breed)")
    violet.add("Aipom")
    violet.add("Misdreavus")
    violet.add("Gulpin")
    violet.add("Swalot")
    violet.add("Bagon")
    violet.add("Shelgon")
    violet.add("Salamence")
    violet.add("Shieldon")
    violet.add("Bastiodon")
    violet.add("Ambipom")
    violet.add("Mismagius")
    violet.add("Clauncher")
    violet.add("Clawitzer")
    violet.add("Passimian")
    violet.add("Morpeko")
    violet.add("Dreepy")
    violet.add("Drakloak")
    violet.add("Dragapult")
    violet.add("Eiscue")
    violet.add("Ceruledge")
    violet.add("Iron Treads")
    violet.add("Iron Bundle")
    violet.add("Iron Hands")
    violet.add("Iron Jugulis")
    violet.add("Iron Moth")
    violet.add("Iron Thorns")
    violet.add("Iron Valiant")
    violet.add("Miraidon")
    violet.add("Iron Leaves")
    violet.add("Iron Boulder")
    violet.add("Iron Crown")

    scarlet_pkmn = any(string_input.strip().lower() == pkmn.strip().lower() for pkmn in scarlet)
    violet_pkmn = any(string_input.strip().lower() == pkmn.strip().lower() for pkmn in violet)
    if scarlet_pkmn:
        return "scarlet"
    elif violet_pkmn:
        return "violet"
    else:
        return "none"