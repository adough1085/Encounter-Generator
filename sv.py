import random
import modules.name_conventions.nc as nc
import numpy as np

            
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
        :param dupes: List of Strings representing Pokemon in the form "Name_Typestring" such as "Pikachu_Electric" or "Charizard_Fire_Flying".
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
        found = any(pkmn_to_check.lower() == dupe.lower() for dupe in dupes)
        return found

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

        alphabetical = {}
        alphabetical[1] = alfornada_cavern
        alphabetical[2] = asado_desert
        alphabetical[3] = cabo_poco
        alphabetical[4] = casseroya_lake
        alphabetical[5] = dalizapa_passage
        alphabetical[6] = east_paldean_sea
        alphabetical[7] = east_province_area_one
        alphabetical[8] = east_province_area_two
        alphabetical[9] = east_province_area_three
        alphabetical[10] = glaseado_mountain
        alphabetical[11] = great_crater_of_paldea
        alphabetical[12] = inlet_grotto
        alphabetical[13] = north_paldean_sea
        alphabetical[14] = north_province_area_one
        alphabetical[15] = north_province_area_two
        alphabetical[16] = north_province_area_three
        alphabetical[17] = poco_path
        alphabetical[18] = pokemon_league
        alphabetical[19] = socarrat_trail
        alphabetical[20] = south_paldean_sea
        alphabetical[21] = south_province_area_one
        alphabetical[22] = south_province_area_two
        alphabetical[23] = south_province_area_three
        alphabetical[24] = south_province_area_four
        alphabetical[25] = south_province_area_five
        alphabetical[26] = south_province_area_six
        alphabetical[27] = tagtree_thicket
        alphabetical[28] = west_paldean_sea
        alphabetical[29] = west_province_area_one
        alphabetical[30] = west_province_area_two
        alphabetical[31] = west_province_area_three


        chronological = {}
        chronological[1] = cabo_poco
        chronological[2] = poco_path
        chronological[3] = inlet_grotto
        chronological[4] = south_province_area_one
        chronological[5] = south_province_area_two
        chronological[6] = pokemon_league
        chronological[7] = south_province_area_three
        chronological[8] = west_province_area_one
        chronological[9] = south_paldean_sea
        chronological[10] = south_province_area_four
        chronological[11] = south_province_area_five
        chronological[12] = east_province_area_one
        chronological[13] = east_province_area_two
        chronological[14] = east_province_area_three
        chronological[15] = tagtree_thicket
        chronological[16] = west_province_area_two
        chronological[17] = west_province_area_three
        chronological[18] = east_paldean_sea
        chronological[19] = west_paldean_sea
        chronological[20] = dalizapa_passage
        chronological[21] = glaseado_mountain
        chronological[22] = alfornada_cavern
        chronological[23] = south_province_area_six
        chronological[24] = asado_desert
        chronological[25] = north_province_area_three
        chronological[26] = north_province_area_two
        chronological[27] = north_province_area_one
        chronological[28] = north_paldean_sea
        chronological[29] = casseroya_lake
        chronological[30] = socarrat_trail
        chronological[31] = great_crater_of_paldea
        
        pair = [chronological, alphabetical]
        return pair

class Game:
    def __init__(self, game):
        self.game = game.strip().lower().capitalize()
        self.areas = []
        self.box = []
        self.dupes = []
        self.links = []
        self.pokedex = []
        self.alphabetical = {}
        self.chronological = {}

        f = open("data/pokedex/paldea_dex.txt", "r")
        self.pokedex = f.readlines()
        f.close()
        
        for x in range(len(self.pokedex)):
            self.pokedex[x] = self.pokedex[x][0:len(self.pokedex[x])-1].strip()
        
        self.define_links()
        self.load_areas()
        


    def define_links(self):
        self.links.append([self.pokedex[0],self.pokedex[1],self.pokedex[2]]) # Sprigatito
        self.links.append([self.pokedex[3],self.pokedex[4],self.pokedex[5]]) # Fuecoco
        self.links.append([self.pokedex[6],self.pokedex[7],self.pokedex[8]]) # Quaxly
        self.links.append([self.pokedex[9],"Oinkologne (Male)","Oinkologne (Female)"]) # Lechonk
        self.links.append([self.pokedex[11],self.pokedex[12]]) # Tarountula
        self.links.append([self.pokedex[13],self.pokedex[14]]) # Nymble
        self.links.append([self.pokedex[15],self.pokedex[16],self.pokedex[17]]) # Hoppip
        self.links.append([self.pokedex[18],self.pokedex[19],self.pokedex[20]]) # Fletchling
        self.links.append([self.pokedex[21],self.pokedex[22],self.pokedex[23]]) # Pawmi
        self.links.append([self.pokedex[24],self.pokedex[25]]) # Houndour
        self.links.append([self.pokedex[26],self.pokedex[27]]) # Yungoos
        self.links.append([self.pokedex[28],self.pokedex[29]]) # Skwovet
        self.links.append([self.pokedex[30],self.pokedex[31]]) # Sunkern
        self.links.append([self.pokedex[32],self.pokedex[33]]) # Kricketot
        self.links.append([self.pokedex[34],self.pokedex[35],self.pokedex[36]]) # Scatterbug
        self.links.append([self.pokedex[37],self.pokedex[38]]) # Combee
        self.links.append([self.pokedex[39],self.pokedex[40],self.pokedex[41]]) # Rookidee
        self.links.append([self.pokedex[42],self.pokedex[43],self.pokedex[44]]) # Happiny
        self.links.append([self.pokedex[45],self.pokedex[46],self.pokedex[47]]) # Azurill
        self.links.append([self.pokedex[48],self.pokedex[49]]) # Surskit
        self.links.append([self.pokedex[50],self.pokedex[51]]) # Buizel
        self.links.append([self.pokedex[52],self.pokedex[53]]) # Wooper
        self.links.append([self.pokedex[54],self.pokedex[55]]) # Psyduck
        self.links.append([self.pokedex[56],self.pokedex[57]]) # Chewtle
        self.links.append([self.pokedex[58],self.pokedex[59],self.pokedex[60]]) # Igglybuff
        self.links.append([self.pokedex[61],self.pokedex[62],self.pokedex[63],self.pokedex[64]]) # Ralts
        self.links.append([self.pokedex[65],self.pokedex[66]]) # Drowzee
        self.links.append([self.pokedex[67],self.pokedex[68],self.pokedex[69]]) # Gastly
        self.links.append([self.pokedex[70],self.pokedex[71]]) # Tandemaus
        self.links.append([self.pokedex[72],self.pokedex[73],self.pokedex[74]]) # Pichu
        self.links.append([self.pokedex[75],self.pokedex[76]]) # Fidough
        self.links.append([self.pokedex[77],self.pokedex[78],self.pokedex[79]]) # Slakoth
        self.links.append([self.pokedex[80],self.pokedex[81],self.pokedex[82]]) # Bounsweet
        self.links.append([self.pokedex[83],self.pokedex[84],self.pokedex[85]]) # Smoliv
        self.links.append([self.pokedex[86],self.pokedex[87]]) # Bonsly
        self.links.append(["Rockruff (Standard)", "Rockruff (Own Tempo)","Lycanroc (Midday)","Lycanroc (Midnight)","Lycanroc (Dusk)"]) # Rockruff
        self.links.append([self.pokedex[90],self.pokedex[91],self.pokedex[92]]) # Rolycoly
        self.links.append([self.pokedex[93],self.pokedex[94],self.pokedex[95]]) # Shinx
        self.links.append([self.pokedex[96],self.pokedex[97],self.pokedex[98]]) # Starly
        self.links.append(["Oricorio (Pom-Pom Style)","Oricorio (Baile Style)"]) # Oricorio
        self.links.append([self.pokedex[100],self.pokedex[101],self.pokedex[102]]) # Mareep
        self.links.append([self.pokedex[103],self.pokedex[104]]) # Petilil
        self.links.append([self.pokedex[105],self.pokedex[106]]) # Shroomish
        self.links.append([self.pokedex[107],self.pokedex[108],self.pokedex[109]]) # Applin
        self.links.append([self.pokedex[110],self.pokedex[111]]) # Spoink
        self.links.append([self.pokedex[112]]) # Squawkabilly
        self.links.append([self.pokedex[113]+" (Violet)",self.pokedex[114]+" (Violet)"]) # Misdreavus
        self.links.append([self.pokedex[115],self.pokedex[116]]) # Makuhita
        self.links.append([self.pokedex[117],self.pokedex[118]]) # Crabrawler
        self.links.append([self.pokedex[119],self.pokedex[120]]) # Salandit
        self.links.append([self.pokedex[121],self.pokedex[122]]) # Phanpy
        self.links.append([self.pokedex[123],self.pokedex[124]]) # Cufant
        self.links.append([self.pokedex[125],self.pokedex[126],self.pokedex[127]]) # Gible
        self.links.append([self.pokedex[128],self.pokedex[129],self.pokedex[130]]) # Nacli
        self.links.append([self.pokedex[131],self.pokedex[132]]) # Wingull
        self.links.append([self.pokedex[133],self.pokedex[134]]) # Magikarp
        self.links.append([self.pokedex[135],self.pokedex[136]]) # Arrokuda
        self.links.append(["Basculin (Red-Striped)","Basculin (Blue-Striped)"]) # Basculin
        self.links.append([self.pokedex[138]+" (Violet)",self.pokedex[139]+" (Violet)"]) # Gulpin
        self.links.append([self.pokedex[140],self.pokedex[141]]) # Meowth
        self.links.append([self.pokedex[142]+" (Scarlet)",self.pokedex[143]+" (Scarlet)"]) # Drifloon
        self.links.append([self.pokedex[144],self.pokedex[145],self.pokedex[146]]) # Flabebe
        self.links.append([self.pokedex[147],self.pokedex[148]]) # Diglett
        self.links.append([self.pokedex[149]]) # Torkoal
        self.links.append([self.pokedex[150],self.pokedex[151]]) # Numel
        self.links.append([self.pokedex[152],self.pokedex[153]]) # Bronzor
        self.links.append([self.pokedex[154],self.pokedex[155],self.pokedex[156]]) # Axew
        self.links.append([self.pokedex[157],self.pokedex[158],self.pokedex[159]]) # Mankey
        self.links.append([self.pokedex[160],self.pokedex[161]]) # Meditite
        self.links.append([self.pokedex[162],self.pokedex[163]]) # Riolu
        self.links.append([self.pokedex[164],self.pokedex[165]+" (Scarlet)",self.pokedex[166]+" (Violet)"]) # Charcadet
        self.links.append([self.pokedex[167],self.pokedex[168]]) # Barboach
        self.links.append([self.pokedex[169],self.pokedex[170]]) # Tadbulb
        self.links.append([self.pokedex[171],self.pokedex[172],self.pokedex[173]]) # Goomy
        self.links.append([self.pokedex[174],self.pokedex[175]]) # Croagunk
        self.links.append([self.pokedex[176],self.pokedex[177]]) # Wattrel
        self.links.append([self.pokedex[178],self.pokedex[179],self.pokedex[180],self.pokedex[181],self.pokedex[182],self.pokedex[183],self.pokedex[184],self.pokedex[185],self.pokedex[186]]) # Eevee
        self.links.append([self.pokedex[187],self.pokedex[188]]) # Dunsparce
        self.links.append([self.pokedex[189],self.pokedex[190]]) # Deerling
        self.links.append([self.pokedex[191],self.pokedex[192]]) # Girafarig
        self.links.append([self.pokedex[193],self.pokedex[194]]) # Grimer
        self.links.append([self.pokedex[195],self.pokedex[196]]) # Maschiff
        self.links.append([self.pokedex[197],self.pokedex[198]]) # Toxel
        self.links.append([self.pokedex[199]]) # Dedenne
        self.links.append([self.pokedex[200]]) # Pachirisu
        self.links.append([self.pokedex[201],self.pokedex[202]]) # Shroodle
        self.links.append([self.pokedex[203]]) # Stantler
        self.links.append([self.pokedex[204],self.pokedex[205]]) # Foongus
        self.links.append([self.pokedex[206],self.pokedex[207]]) # Voltorb
        self.links.append([self.pokedex[208],self.pokedex[209],self.pokedex[210]]) # Magnemite
        self.links.append([self.pokedex[211]]) # Ditto
        self.links.append([self.pokedex[212],self.pokedex[213]]) # Growlithe
        self.links.append([self.pokedex[214],self.pokedex[215]]) # Teddiursa
        self.links.append([self.pokedex[216]]) # Zangoose
        self.links.append([self.pokedex[217]]) # Seviper
        self.links.append([self.pokedex[218],self.pokedex[219]]) # Swablu
        self.links.append([self.pokedex[220],self.pokedex[221]]) # Skiddo
        self.links.append(["Tauros (Combat Breed)", "Tauros (Blaze Breed) (Scarlet)","Tauros (Aqua Breed) (Violet)"]) # Tauros
        self.links.append([self.pokedex[223],self.pokedex[224]]) # Litleo
        self.links.append([self.pokedex[225]+" (Scarlet)",self.pokedex[226]+" (Scarlet)"]) # Stunky
        self.links.append([self.pokedex[227],self.pokedex[228]]) # Zorua
        self.links.append([self.pokedex[229],self.pokedex[230]]) # Sneasel
        self.links.append([self.pokedex[231],self.pokedex[232]]) # Murkrow
        self.links.append([self.pokedex[233],self.pokedex[234],self.pokedex[235]]) # Gothita
        self.links.append([self.pokedex[236],self.pokedex[237]]) # Sinistea
        self.links.append([self.pokedex[238]]) # Mimikyu
        self.links.append([self.pokedex[239]]) # Klefki
        self.links.append([self.pokedex[240]]) # Indeedee
        self.links.append([self.pokedex[241],self.pokedex[242]]) # Bramblin
        self.links.append([self.pokedex[243],self.pokedex[244]]) # Toedscool
        self.links.append([self.pokedex[245]]) # Tropius
        self.links.append([self.pokedex[246],self.pokedex[247]]) # Fomantis
        self.links.append([self.pokedex[248]]) # Klawf
        self.links.append([self.pokedex[249],self.pokedex[250]]) # Capsakid
        self.links.append([self.pokedex[251],self.pokedex[252]]) # Cacnea
        self.links.append([self.pokedex[253],self.pokedex[254]]) # Rellor
        self.links.append([self.pokedex[255],self.pokedex[256]]) # Venonat
        self.links.append([self.pokedex[257],self.pokedex[258]]) # Pineco
        self.links.append([self.pokedex[259],self.pokedex[260]]) # Scyther
        self.links.append([self.pokedex[261]]) # Heracross
        self.links.append([self.pokedex[262],self.pokedex[263]]) # Flittle
        self.links.append([self.pokedex[264],self.pokedex[265]]) # Hippopotas
        self.links.append([self.pokedex[266],self.pokedex[267],self.pokedex[268]]) # Sandile
        self.links.append([self.pokedex[269],self.pokedex[270]]) # Silicobra
        self.links.append([self.pokedex[271],self.pokedex[272]]) # Mudbray
        self.links.append([self.pokedex[273],self.pokedex[274]]) # Larvesta
        self.links.append([self.pokedex[275]+" (Violet)",self.pokedex[276]+" (Violet)",self.pokedex[277]+" (Violet)"]) # Bagon
        self.links.append([self.pokedex[278],self.pokedex[279],self.pokedex[280]]) # Tinkatink
        self.links.append([self.pokedex[281],self.pokedex[282],self.pokedex[283]]) # Hatenna
        self.links.append([self.pokedex[284],self.pokedex[285],self.pokedex[286]]) # Impidimp
        self.links.append([self.pokedex[287],self.pokedex[288]]) # Wiglett
        self.links.append([self.pokedex[289]]) # Bombirdier
        self.links.append([self.pokedex[290],self.pokedex[291]]) # Finizen
        self.links.append([self.pokedex[292],self.pokedex[293]]) # Varoom
        self.links.append([self.pokedex[294]]) # Cyclizar
        self.links.append([self.pokedex[295]]) # Orthworm
        self.links.append([self.pokedex[296]]) # Sableye
        self.links.append([self.pokedex[297],self.pokedex[298]]) # Shuppet
        self.links.append([self.pokedex[299]]) # Falinks
        self.links.append([self.pokedex[300]]) # Hawlucha
        self.links.append([self.pokedex[301]]) # Spiritomb
        self.links.append([self.pokedex[302],self.pokedex[303]]) # Noibat
        self.links.append([self.pokedex[304]+" (Violet)",self.pokedex[305]+" (Violet)",self.pokedex[306]+" (Violet)"]) # Dreepy
        self.links.append([self.pokedex[307],self.pokedex[308]]) # Glimmet
        self.links.append([self.pokedex[309]]) # Rotom
        self.links.append([self.pokedex[310],self.pokedex[311]]) # Greavard
        self.links.append([self.pokedex[312]+" (Scarlet)"]) # Oranguru
        self.links.append([self.pokedex[313]+" (Violet)"]) # Passimian
        self.links.append([self.pokedex[314]]) # Komala
        self.links.append([self.pokedex[315]+" (Scarlet)",self.pokedex[316]+" (Scarlet)",self.pokedex[317]+" (Scarlet)"]) # Larvitar
        self.links.append([self.pokedex[318]+" (Scarlet)"]) # Stonjourner
        self.links.append([self.pokedex[319]+" (Violet)"]) # Eiscue
        self.links.append([self.pokedex[320]]) # Pincurchin
        self.links.append([self.pokedex[321],self.pokedex[322]]) # Sandygast
        self.links.append([self.pokedex[323],self.pokedex[324],self.pokedex[325]]) # Slowpoke
        self.links.append([self.pokedex[326],self.pokedex[327]]) # Shellder
        self.links.append([self.pokedex[330]]) # Qwilfish
        self.links.append([self.pokedex[331]]) # Luvdisc
        self.links.append([self.pokedex[332],self.pokedex[333]]) # Finneon
        self.links.append([self.pokedex[334]]) # Bruxish
        self.links.append([self.pokedex[335]]) # Alomomola
        self.links.append([self.pokedex[336]+" (Scarlet)",self.pokedex[337]+" (Scarlet)"]) # Skrelp
        self.links.append([self.pokedex[338]+" (Violet)",self.pokedex[339]+" (Violet)"]) # Clauncher
        self.links.append([self.pokedex[340],self.pokedex[341],self.pokedex[342]]) # Tynamo
        self.links.append([self.pokedex[343],self.pokedex[344]]) # Mareanie
        self.links.append([self.pokedex[345]]) # Flamigo
        self.links.append([self.pokedex[346],self.pokedex[347],self.pokedex[348]]) # Dratini
        self.links.append([self.pokedex[349],self.pokedex[350]]) # Snom
        self.links.append([self.pokedex[351],self.pokedex[352]]) # Snover
        self.links.append([self.pokedex[353]]) # Delibird
        self.links.append([self.pokedex[354],self.pokedex[355]]) # Cubchoo
        self.links.append([self.pokedex[356],self.pokedex[357],self.pokedex[358]]) # Snorunt
        self.links.append([self.pokedex[359]]) # Cryogonal
        self.links.append([self.pokedex[360],self.pokedex[361]])  # Cetoddle
        self.links.append([self.pokedex[362],self.pokedex[363]]) # Bergmite
        self.links.append([self.pokedex[364],self.pokedex[365]]) # Rufflet
        self.links.append([self.pokedex[366],self.pokedex[367],self.pokedex[368]]) # Pawniard
        self.links.append([self.pokedex[369]+" (Scarlet)",self.pokedex[370]+" (Scarlet)",self.pokedex[371]+" (Scarlet)"]) # Deino
        self.links.append([self.pokedex[372]]) # Veluza
        self.links.append([self.pokedex[373]]) # Dondozo
        self.links.append([self.pokedex[374]]) # Tatsugiri
        self.links.append([self.pokedex[375]+" (Scarlet)"]) # Great Tusk
        self.links.append([self.pokedex[376]+" (Scarlet)"]) # Scream Tail
        self.links.append([self.pokedex[377]+" (Scarlet)"]) # Brute Bonnet 
        self.links.append([self.pokedex[378]+" (Scarlet)"]) # Flutter Mane 
        self.links.append([self.pokedex[379]+" (Scarlet)"]) # Slither Wing 
        self.links.append([self.pokedex[380]+" (Scarlet)"]) # Sandy Shocks 
        self.links.append([self.pokedex[381]+" (Violet)"]) # Iron Treads
        self.links.append([self.pokedex[382]+" (Violet)"]) # Iron Bundle
        self.links.append([self.pokedex[383]+" (Violet)"]) # Iron Hands
        self.links.append([self.pokedex[384]+" (Violet)"]) # Iron Jugulis
        self.links.append([self.pokedex[385]+" (Violet)"]) # Iron Moth
        self.links.append([self.pokedex[386]+" (Violet)"]) # Iron Thorns
        self.links.append([self.pokedex[387],self.pokedex[388],self.pokedex[389]]) # Frigibax
        self.links.append([self.pokedex[390],self.pokedex[391]]) # Gimmighoul
        self.links.append([self.pokedex[392]]) # Wo-Chien
        self.links.append([self.pokedex[393]]) # Chien-Pao
        self.links.append([self.pokedex[394]]) # Ting-Li
        self.links.append([self.pokedex[395]]) # Chi-Yu
        self.links.append([self.pokedex[396]+" (Scarlet)"]) # Roaring Moon
        self.links.append([self.pokedex[397]+" (Violet)"]) # Iron Valiant
        self.links.append([self.pokedex[398]+" (Scarlet)"]) # Koraidon
        self.links.append([self.pokedex[399]+" (Violet)"]) # Miraidon

    def dupe_out(self):
        found = False
        for boxed_mon in self.box:
            for link in self.links:
                for pkmn in link:
                    if boxed_mon.strip().lower() == pkmn.strip().lower():
                        found = True
                    if found == True:
                        for x in link:
                            self.dupes.append(x)
                        break
                if found == True:
                    found = False
                    break 

    def generate(self, pkmn_set_int, area, time, type, power, check_dupes):
        pkmn_set = {}
        area_chosen = -1
        daypart = ""
        if pkmn_set_int == 0:
            pkmn_set = self.chronological
        elif pkmn_set_int == 1:
            pkmn_set = self.alphabetical
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None

        if 1 <= area and area <= 31:
            area_chosen = area
        else:
            print("Areas 1-31")
            return None

        if time == 0:
            daypart = "Dawn"
        elif time == 1:
            daypart = "Day"
        elif time == 2:
            daypart = "Dusk"
        elif time == 3:
            daypart = "Night"
        else:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None
        
        pkmn_set[area_chosen].generate(self.game, daypart, type, power, self.dupes, check_dupes)

    def distribution(self, pkmn_set_int, area, time, type, power, check_dupes):
        pkmn_set = {}
        area_chosen = -1
        daypart = ""
        if pkmn_set_int == 0:
            pkmn_set = self.chronological
        elif pkmn_set_int == 1:
            pkmn_set = self.alphabetical
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None

        if 1 <= area and area <= 31:
            area_chosen = area
        else:
            print("Areas 1-31")
            return None

        if time == 0:
            daypart = "Dawn"
        elif time == 1:
            daypart = "Day"
        elif time == 2:
            daypart = "Dusk"
        elif time == 3:
            daypart = "Night"
        else:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None
        
        pkmn_set[area_chosen].distribution(self.game, daypart, type, power, self.dupes, check_dupes)

    def locate(self, pkmn_set_int, pkmn):
        if pkmn_set_int == 0:
            pkmn_set = self.chronological
        elif pkmn_set_int == 1:
            pkmn_set = self.alphabetical
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None
        
        habitats = []
        for x in range(len(pkmn_set)):
            pkmn_found = False
            dawn_found = False
            day_found = False
            dusk_found = False
            night_found = False
            for k in pkmn_set[x+1].dawn.keys():
                if k.lower().find(pkmn.lower().strip()) != -1:
                    pkmn_found = True
                    break
            if pkmn_found == False:
                continue
            elif pkmn_found == True:
                for k in pkmn_set[x+1].dawn.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].dawn[k] > 0:
                        dawn_found = True
                        break
                for k in pkmn_set[x+1].day.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].day[k] > 0:
                        day_found = True
                        break
                for k in pkmn_set[x+1].dusk.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].dusk[k] > 0:
                        dusk_found = True
                        break
                for k in pkmn_set[x+1].night.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].night[k] > 0:
                        night_found = True
                        break
            if (dawn_found == True) and (day_found == True) and (dusk_found == True) and (night_found == True):
                habitats.append(pkmn_set[x+1].name)
            else:
                string = pkmn_set[x+1].name + " ("
                if dawn_found == True:
                    string = string + "Dawn, "
                if day_found == True:
                    string = string + "Day, "
                if dusk_found == True:
                    string = string + "Dusk, "
                if night_found == True:
                    string = string + "Night, "
                string = string[0:len(string)-2] + ")"
                habitats.append(string)
        if len(habitats) >= 1:
            print("{0} is located in:".format(pkmn))
            for x in habitats:
                print(x)

    def load_areas(self):
        duo = Area.load_areas()
        self.alphabetical = duo[1]
        self.chronological = duo[0]

g = Game("Scarlet")
g.box = ["Crocalor","Clodsire","Gumshoos","Arrokuda","Klawf","Bombirdier", "Magikarp", "Gimmighoul","Azumarill","Oinkologne (Male)","Tauros (Combat Breed)", "Goomy","Basculin (Red-Striped)"]
g.dupe_out()
g.distribution(0,15,1,"Flying",0,True)
g.generate(0,15,1,"Flying",0,True)
#g.generate(0,8,1,"Flying",0)
#g.distribution(0,9,1,"Normal",0)
#g.generate(0,15,1,"Fairy",1)
#g.locate(0, "Dratini")