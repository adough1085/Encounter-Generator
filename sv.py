import random
import modules.name_conventions.nc as nc
import modules.validation.v as v

class Area:
    def __init__(self, name):
        self.name = nc.standard(name)
        self.snake_case_name = nc.snake_case(name)
        self.pokemon = []
        self.dawn = {}
        self.day = {}
        self.dusk = {}
        self.night = {}
        self.biome_multipliers = {}
        self.load_biome_multipliers()
        self.load_inserts()

    def load_biome_multipliers(self):
        file_path = f"data/distribution/{self.snake_case_name}.csv"
        lines = ""
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for x in range(len(lines)-1):
            line = lines[x+1].split(",")
            biome = line[0]
            percentage = line[1][:len(line[1])-1] # This extra code is to remove the \n at the end of percentage
            self.biome_multipliers[biome] = float(percentage)

    def power(self, power):
        upper_bound = 0
        if power == 1:
            upper_bound = 50
        elif power == 2:
            upper_bound = 75
        elif power == 3: 
            upper_bound = 100
        else:
            return False
        
        if random.randint(1,100) <= upper_bound:
            return True
        else:
            return False

    def parse_insert(self, insert_string):
        # insert_string should look something like: Dugtrio,Ground,Ground,Cave,20,20,20,20
        line = insert_string.split(",")
        name = line[0]
        type1 = line[1]
        type2 = line[2]
        biome = line[3]
        multiplier = self.biome_multipliers[biome]
        dawn = int(line[4])*multiplier
        day = int(line[5])*multiplier
        dusk = int(line[6])*multiplier
        night = int(line[7])*multiplier
        type_string = type1

        if type1 != type2:
            type_string = f"{type_string}_{type2}"

        # identifier will end up looking something like: Dugtrio_Ground
        identifier = f"{name}_{type_string}"

        
        if self.find_key(identifier) == False:
            self.pokemon.append(identifier)
            self.dawn[identifier] = dawn
            self.day[identifier] = day
            self.dusk[identifier] = dusk
            self.night[identifier] = night
        else:
            self.dawn[identifier] = self.dawn[identifier] + dawn
            self.day[identifier] = self.day[identifier] + day
            self.dusk[identifier] = self.dusk[identifier] + dusk
            self.night[identifier] = self.night[identifier] + night

    def load_inserts(self):
        file_path = f"data/probability_insert/{self.snake_case_name}.csv"
        lines = ""
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for x in range(len(lines)-1):
            line = lines[x+1]
            line = line[:len(line)-1]
            self.parse_insert(line)

    def find_key(self, pkmn_to_check):
        """
        Docstring for find_key
        
        :param self: Area object.
        :param pkmn_to_check: String representing the Pokemon that is being checked if it already exists.

        This function will check if this self.pokemon being inquired has already been recorded in this area.
        This function is used because dictionaries are used in the case of sum + addend.
        Dictionaries will throw an error in the case above if the key does not already exist.
        Hence, the need for this function.
        """
        # Compare the Pokemon to be checked to every Pokemon recorded in the area
        # Return whether or not the Pokemon was found
        # Names are compared in lowercase in case of any strange case input errors. 
        found = any(pkmn_to_check.lower() == recorded_pkmn.lower() for recorded_pkmn in self.pokemon)
        return found
    
    def find_dupe(self, dupes, pkmn_to_check, rule_enabled):
        """
        Docstring for find_dupe
        
        :param self: Area object.
        :param dupes: Set of Strings representing Pokemon in the form "Name_Typestring" such as "Pikachu_Electric" or "Charizard_Fire_Flying". Typically, argument will be "dupes" set recorded by Game object.
        :param pkmn_to_check: String representing the Pokemon that is being checked if it already exists.
        :param rule_enabled: Boolean that signifies if the function will perform any operations. 

        "Dupe" is short for "duplication", and is in reference to a Pokemon (or evolutionary related Pokemon) that you already have CAPTURED before.
        This is related to a common optional rule called "Dupes Clause", which is explained below.which means if you encounter a Pokemon,
        if it is a duplicate then you can ignore it and encounter a different Pokemon, 
        where that Pokemon can also be ignored as per Dupes Clause rules.
        This continues until you encounter a Pokemon (nor any of its evolutionary related Pokemon) that has not been CAPTURED before.

        Dupes Clause is a common optional rule that states:
            - A Pokemon (or its evolutionary-related Pokemon) that you have already captured before are "dupes" or duplicates
            - If encountering a dupe, the dupe can be ignored and you can attempt another encounter
            - This continues until finding a non-dupe
        
        Dupes Clause is used to:
            - Add uniqueness to the roster that you build
            - Add difficulty by making Pokemon irreplaceable
        """
        # Redundancy to check if rule_enabled is a Boolean 
        rule_enabled = (rule_enabled) if (True | False) else (False)

        if rule_enabled == False:
            return False

        # Compare the Pokemon to be checked to every Pokemon in the dupes list
        # Return whether or not the Pokemon is a dupe
        # Names are compared in lowercase in case of any strange case input errors.
        return any(pkmn_to_check == dupe.lower() for dupe in dupes)

    def distribution(self, game, time, type, power, dupes, check_dupes):

        # Choosing all possible wild Pokemon that are present within the day part selected.
        time = time.lower().strip()
        print("{0} ({1})".format(self.name,time.capitalize()))
        selected = {}
        if time == "dawn":
            selected = self.dawn
        elif time == "day":
            selected = self.day
        elif time == "dusk":
            selected = self.dusk
        elif time == "night":
            selected = self.night

        # Ensures that types entered are legitimate types, and will ignore typos.
        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        valid_type = False
        for t in types:
            if type.strip().lower() == t.strip().lower():
                valid_type = True
                break
        
        """
        I am under the assumption that the way Encounter Powers works is: 
        whatever % of encounters will be the enforced type, while the other % will always be a different type.
        I have yet to find extensive evidence that proves or disproves this, but it is a simpler assumption
        compared to the possibility that the other % still having a chance to spawn the enforced type.
        """
        upper_bound = 0
        if power >= 1 and power <= 3 and valid_type == True:
            if power == 1:
                upper_bound = 0.50
            elif power == 2:
                upper_bound = 0.75
            elif power == 3: 
                upper_bound = 1
        multiplier = (1-upper_bound)

        sum = 0
        keys = selected.keys() # Keys are possible wild Pokemon present in the day part selected.
        for k in keys: # For every while Pokemon
            if self.find_dupe(dupes, k.split("_")[0], check_dupes) == False: # Proceed if neither the Pokemon (or related Pokemon) have already been captured
                if game == "Scarlet" and k.find("Violet") == -1: # Proceed if the Pokemon is not an opposite version exclusive 
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1: # If there is an Encounter Power in use and the Pokemon is not of the correct type,
                        sum = sum + selected[k]*multiplier # Apply the multiplier (actually makes chances worse for incorrect type pokemon)
                    else:
                        sum = sum + selected[k]
                elif game == "Violet" and k.find("Scarlet") == -1:
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        sum = sum + selected[k]*multiplier
                    else:
                        sum = sum + selected[k]
        
        names = []
        percents = []
        for k in keys:
            if self.find_dupe(dupes, k.split("_")[0], check_dupes) == False:
                if game == "Scarlet" and k.find("Violet") == -1:
                    n = k.split("_")[0]
                    percent = 0
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        percent = selected[k]*multiplier/sum
                    else:
                        percent = selected[k]/sum
                    index = -1
                    percent = percent * 10000
                    percent = percent // 1
                    percent = percent / 100
                    if len(percents) == 0:
                        index = 0
                    else:
                        for x in range(len(percents)):
                            if percent >= percents[x]:
                                index = x
                                break
                        if index == -1:
                            index = len(percents)
                    names.insert(index, n)
                    percents.insert(index, percent)
                elif game == "Violet" and k.find("Scarlet") == -1:
                    n = k.split("_")[0]
                    percent = 0
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        percent = selected[k]*multiplier/sum
                    else:
                        percent = selected[k]/sum
                    index = 0
                    percent = percent * 10000
                    percent = percent // 1
                    percent = percent / 100
                    if len(percents) == 0:
                        continue
                    else:
                        for x in range(len(percents)):
                            if percent >= percents[x]:
                                index = x
                                break
                            index = len(percents)-1
                    names.insert(index, n)
                    percents.insert(index, percent)
        for x in range(len(names)):
            print("{0}: {1}%".format(names[x],percents[x]))        

    def generate(self, game, time, type, power, dupes, check_dupes):
        class Range:
            def __init__(self, name, lower, upper):
                self.name = name
                self.lower = lower
                self.upper = upper

            def enclosed(self, number):
                return (self.lower <= number and number <= self.upper)             

        # Ensures that types entered are legitimate types, and will ignore typos.
        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        valid_type = False
        for t in types:
            if type.strip().lower() == t.strip().lower():
                valid_type = True
                break
        
        # If the type entered is real, then check if the specific type is activated.
        power_activated = False
        if valid_type == True:
            power_activated = self.power(power)

        # Select a day part
        time = time.lower().strip()
        selected = {}
        if time == "dawn":
            selected = self.dawn
        elif time == "day":
            selected = self.day
        elif time == "dusk":
            selected = self.dusk
        elif time == "night":
            selected = self.night

        sum = 0
        keys = selected.keys() # Keys are possible wild Pokemon present in the day part selected.
        ranges = []

        for k in keys: # For every wild Pokemon
            if self.find_dupe(dupes, k.split("_")[0], check_dupes) == False: # Proceed if neither the Pokemon (or related Pokemon) have already been captured
                if game == "Scarlet" and k.find("Violet") == -1: # Proceed if the Pokemon is not an opposite version exclusive 
                    if power_activated == True and k.find(type) == -1: # Skip if a specific type is enforced, and the Pokemon does not match the type.
                        continue
                    ranges.append(Range(k, sum, sum + selected[k])) # Otherwise, create ranges with bounds like: [(0, 15.7563), (15.7563, 26.0), etc.]
                    sum = sum + selected[k]
                elif game == "Violet" and k.find("Scarlet") == -1:
                    if power_activated == True and k.find(type) == -1:
                        continue
                    ranges.append(Range(k, sum, sum + selected[k]))
                    sum = sum + selected[k]
    
        rng = random.uniform(0, sum) # Generate a value
        for r in ranges: # For every range created...
            if r.enclosed(rng): # Proceed if the value falls within the range
                pkmn_name = r.name.split("_")[0]
                print(f"{self.name} ({time.title()}): {pkmn_name}")
                return r.name

    def load_areas():
        alfornada_cavern = Area("Alfornada Cavern")
        asado_desert = Area("Asado Desert")
        cabo_poco = Area("Cabo Poco")
        casseroya_lake = Area("Casseroya Lake")
        dalizapa_passage = Area("Dalizapa Passage")
        east_paldean_sea = Area("East Paldean Sea")
        east_province_area_one = Area("East Province (Area One)")
        east_province_area_two = Area("East Province (Area Two)")
        east_province_area_three = Area("East Province (Area Three)")
        glaseado_mountain = Area("Glaseado Mountain")
        great_crater_of_paldea = Area("Great Crater of Paldea")
        inlet_grotto = Area("Inlet Grotto")
        north_paldean_sea = Area("North Paldean Sea")
        north_province_area_one = Area("North Province (Area One)")
        north_province_area_two = Area("North Province (Area Two)")
        north_province_area_three = Area("North Province (Area Three)")
        poco_path = Area("Poco Path")
        pokemon_league = Area("Pokemon League")
        socarrat_trail = Area("Socarrat Trail")
        south_paldean_sea = Area("South Paldean Sea")
        south_province_area_one = Area("South Province (Area One)")
        south_province_area_two = Area("South Province (Area Two)")
        south_province_area_three = Area("South Province (Area Three)")
        south_province_area_four = Area("South Province (Area Four)")
        south_province_area_five = Area("South Province (Area Five)")
        south_province_area_six = Area("South Province (Area Six)")
        tagtree_thicket = Area("Tagtree Thicket")
        west_paldean_sea = Area("West Paldean Sea")
        west_province_area_one = Area("West Province (Area One)")
        west_province_area_two = Area("West Province (Area Two)")
        west_province_area_three = Area("West Province (Area Three)")

        numerical = {}
        numerical[1] = alfornada_cavern
        numerical[2] = asado_desert
        numerical[3] = cabo_poco
        numerical[4] = casseroya_lake
        numerical[5] = dalizapa_passage
        numerical[6] = east_paldean_sea
        numerical[7] = east_province_area_one
        numerical[8] = east_province_area_two
        numerical[9] = east_province_area_three
        numerical[10] = glaseado_mountain
        numerical[11] = great_crater_of_paldea
        numerical[12] = inlet_grotto
        numerical[13] = north_paldean_sea
        numerical[14] = north_province_area_one
        numerical[15] = north_province_area_two
        numerical[16] = north_province_area_three
        numerical[17] = poco_path
        numerical[18] = pokemon_league
        numerical[19] = socarrat_trail
        numerical[20] = south_paldean_sea
        numerical[21] = south_province_area_one
        numerical[22] = south_province_area_two
        numerical[23] = south_province_area_three
        numerical[24] = south_province_area_four
        numerical[25] = south_province_area_five
        numerical[26] = south_province_area_six
        numerical[27] = tagtree_thicket
        numerical[28] = west_paldean_sea
        numerical[29] = west_province_area_one
        numerical[30] = west_province_area_two
        numerical[31] = west_province_area_three

        alpha = {}
        alpha["Alfornada Cavern"] = alfornada_cavern
        alpha["Asado Desert"] = asado_desert
        alpha["Cabo Poco"] = cabo_poco
        alpha["Casseroya Lake"] = casseroya_lake
        alpha["Dalizapa Passage"] = dalizapa_passage
        alpha["East Paldean Sea"] = east_paldean_sea
        alpha["East Province (Area One)"] = east_province_area_one
        alpha["East Province (Area Two)"] = east_province_area_two
        alpha["East Province (Area Three)"] = east_province_area_three
        alpha["Glaseado Mountain"] = glaseado_mountain
        alpha["Great Crater of Paldea"] = great_crater_of_paldea
        alpha["Inlet Grotto"] = inlet_grotto
        alpha["North Paldean Sea"] = north_paldean_sea
        alpha["North Province (Area One)"] = north_province_area_one
        alpha["North Province (Area Two)"] = north_province_area_two
        alpha["North Province (Area Three)"] = north_province_area_three
        alpha["Poco Path"] = poco_path
        alpha["Pokemon League"] = pokemon_league
        alpha["Socarrat Trail"] = socarrat_trail
        alpha["South Paldean Sea"] = south_paldean_sea
        alpha["South Province (Area One)"] = south_province_area_one
        alpha["South Province (Area Two)"] = south_province_area_two
        alpha["South Province (Area Three)"] = south_province_area_three
        alpha["South Province (Area Four)"] = south_province_area_four
        alpha["South Province (Area Five)"] = south_province_area_five
        alpha["South Province (Area Six)"] = south_province_area_six
        alpha["Tagtree Thicket"] = tagtree_thicket
        alpha["West Paldean Sea"] = west_paldean_sea
        alpha["West Province (Area One)"] = west_province_area_one
        alpha["West Province (Area Two)"] = west_province_area_two
        alpha["West Province (Area Three)"] = west_province_area_three
        
        pair = [numerical, alpha]
        return pair

class Game:
    def __init__(self, game):
        self.game = game.strip().lower().capitalize()
        self.areas = []
        self.box = []
        self.links = {}
        self.dupes = set()
        self.pokedex = []
        self.alphabetical = {}
        self.numerical = {}

        with open("data/pokedex/paldea_dex.txt","r") as f1:
            self.pokedex = f1.readlines()
        
        for x in range(len(self.pokedex)):
            self.pokedex[x] = self.pokedex[x][0:len(self.pokedex[x])-1].strip()
        
        self.define_links()
        self.load_areas()
        
    def define_links(self):
        links = ""
        with open("data/pokedex/links.txt", "r") as f1:
            links = f1.readlines()
        for line in links:
            pkmn_list = line.strip().split(",")
            header_pkmn = pkmn_list[0]
            linked_pkmn = pkmn_list[1].split("_")
            self.links[header_pkmn] = linked_pkmn

    def populate_dupes(self):
        for boxed_pkmn in self.box:
            link = self.links[boxed_pkmn]
            for pkmn in link:
                self.dupes.add(pkmn)

    def generate(self, area, time, type, power, check_dupes):
        pkmn_set = {}
        if isinstance(area, str):
            area = area.strip()
        if isinstance(time, str):
            time = time.strip()
        

        # Making sure that area input is valid
        if isinstance(area, str):
            if area.isnumeric():
                area = int(area)
            if self.valid_area(area) == False:
                print("Invalid Area")
                return None
        if isinstance(area, int):
            if (1 <= area and area <= 31) == False:
                print("Areas 1-31")
                return None
        
        # Making sure that time input is valid
        daypart = v.resolve_daypart(time)
        if daypart == False:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None

        # Setting area set
        if isinstance(area, int):
            pkmn_set = self.numerical
        else:
            pkmn_set = self.alphabetical
        
        pkmn_set[area].generate(self.game, daypart, type, power, self.dupes, check_dupes)

    def distribution(self, area, time, type, power, check_dupes):
        pkmn_set = {}
        if isinstance(area, str):
            area = area.strip()
        if isinstance(time, str):
            time = time.strip()
        

        # Making sure that area input is valid
        if isinstance(area, str):
            if area.isnumeric():
                area = int(area)
            if self.valid_area(area) == False:
                print("Invalid Area")
                return None
        if isinstance(area, int):
            if (1 <= area and area <= 31) == False:
                print("Areas 1-31")
                return None
        
        # Making sure that time input is valid
        daypart = v.resolve_daypart(time)
        if daypart == False:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None

        # Setting area set
        if isinstance(area, int):
            pkmn_set = self.numerical
        else:
            pkmn_set = self.alphabetical
        
        pkmn_set[area].distribution(self.game, daypart, type, power, self.dupes, check_dupes)

    def locate(self, pkmn):
        pkmn = pkmn.strip().lower()
        areas_dict = self.alphabetical
        habitats = []

        for area in areas_dict.values():
            dawn_found = any(native_pkmn.strip().lower().find(pkmn) for native_pkmn in area.dawn.keys())
            day_found = any(native_pkmn.strip().lower().find(pkmn) for native_pkmn in area.day.keys())
            dusk_found = any(native_pkmn.strip().lower().find(pkmn) for native_pkmn in area.dusk.keys())
            night_found = any(native_pkmn.strip().lower().find(pkmn) for native_pkmn in area.night.keys())

            if dawn_found and day_found and dusk_found and night_found:
                habitats.append(area.name)
            else:
                string = f"{area.name} ("
                if dawn_found:
                    string = f"{string}Dawn, "

                if day_found:
                    string = f"{string}Day, "

                if dusk_found:
                    string = f"{string}Dusk, "

                if night_found:
                    string = f"{string}Night, "

                string = string[0:len(string)-2] + ")"
                habitats.append(string)

        if len(habitats) >= 1:
            print(f"{pkmn.title()} is located in:")
            for x in habitats:
                print(x)

    def load_areas(self):
        duo = Area.load_areas()
        self.alphabetical = duo[1]
        self.numerical = duo[0]

            

g = Game("Scarlet")
g.box = ["Crocalor","Clodsire","Gumshoos","Arrokuda","Klawf","Bombirdier", "Magikarp", "Gimmighoul","Azumarill","Oinkologne (Male)","Tauros (Combat Breed)", "Goomy","Basculin (Red-Striped)"]
g.populate_dupes()
g.distribution(15,1,"Flying",0,True)
g.generate(15,1,"Flying",0,True)
#g.generate(8,1,"Flying",0)
#g.distribution(9,1,"Normal",0)
#g.generate(15,1,"Fairy",1)
g.locate("Dratini")