import random
from modules import nc as nc
from modules import v as v

class Area:
    def __init__(self, name):
        """
        Docstring for __init__
        
        :param self: Area object.
        :param name: String representation of the area name with format: "Alfornada Cavern".

        The name will be standardized such that as long as the name input are words separated by a space, it will become format "Alfornada Cavern".
        snake_case_name will be of format "alfornada cavern".

        pokemon is list of Strings representing Pokemon present in the area.

        The dayparts (dawn, day, dusk, and night) are dictionaries that have the format: K: Pokemon name as str, V: float.
        -  values within the daypart dictionaries are float values such as 11.7306, calculated by an integer value multiplied by biome_multiplier.
        - For example with daypart value calculation: (50 * 0.234612) = 11.7306.
        biome_multipliers is a dictionary that has the format: K: biome name as str, V: float.
        - The values in biome_multipliers represent the amount of percentage that a certain biome covers in comparison to all covered biome square area.
        """
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
        """
        Docstring for load_biome_multipliers
        
        :param self: Area object.

        This function will open the CSV files that have the name format for example "alfornada_cavern.csv".
        The CSV files contain two headers: "Biome", and "Percentage".
        Biome represents the biome name/type.
        Percentage represents what percent the particular biome covers in comparison to all covered biome space.

        This is stored into the Area object's biome_multipliers dictionary with format K: Biome as str, V: Percentage as float
        """
        file_path = f"data/distribution/{self.snake_case_name}.csv"
        lines = ""
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for x in range(len(lines)-1):
            line = lines[x+1].split(",")
            biome = line[0]
            percentage = line[1][:len(line[1])-1] # This extra code is to remove the \n at the end of percentage
            self.biome_multipliers[biome] = float(percentage)

    def parse_insert(self, insert_string):
        """
        Docstring for parse_insert
        
        :param self: Area object.
        :param insert_string: String object that has format like: "Dugtrio,Ground,Ground,Cave,20,20,20,20"

        This function is only meant to be used within the load_insert() function within this Area class.

        insert_string is a String that comes from a CSV file with headers: "Name", "Type1", "Type2", "Biome", "Dawn", "Day", "Dusk", and "Night"
        This function will create identifier, which contains the name of the Pokemon, the version exclusivity (Scarlet or Violet if applicable), and the type(s).
        - If the Pokemon has only one unique type, identifier will look like: "Dugtrio_Ground"
        - If the Pokemon has two unique types, identifer will look like: "Gyarados_Water_Flying"
        - If the Pokemon is a version exclusive (can only be found in a certain version of the game), identifier will look like: "Larvitar (Scarlet)_Rock_Ground"

        Biome is used to return the biome_multiplier value, a float ranging from 0.0 to 1.0, representing percentage that a certain biome covers in comparison to all covered biome square area within an Area.
        The integer values marked by Dawn, Day, etc., are multiplied by biome_multiplier, for example (20 * 1.0 = 20.0).
        Identifier is also as a key value in daypart dictionaries such as dawn["Dugtrio_Ground"] = float value.
        """

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
        """
        Docstring for load_inserts
        
        :param self: Area object.
        
        This function will open a CSV file with headers: "Name", "Type1", "Type2", "Biome", "Dawn", "Day", "Dusk", and "Night".
        Every line will be read, and passed to the parse_insert() function.
        """
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

        rule_enabled = rule_enabled if rule_enabled == True or False else False

        if rule_enabled == False:
            return False

        # Compare the Pokemon to be checked to every Pokemon in the dupes list
        # Return whether or not the Pokemon is a dupe
        # Names are compared in lowercase in case of any strange case input errors.
        return any(pkmn_to_check.lower() == dupe.lower() for dupe in dupes)

    def distribution(self, game, time, type, power, dupes, check_dupes, print_boolean=False):
        """
        Docstring for distribution
        
        :param self: Area object.
        :param game: String object representing game, either "Scarlet" or "Violet".
        :param time: String object that represents the daypart, possible values are: "Dawn", "Day", "Dusk", and "Night".
        :param type: String object that represents a Pokemon Type (Grass, Water, etc.).
        :param power: Integer object ranging from 1, 2, or 3; represents an Encounter Power which increases likelihood of a Pokemon of a specific Type (Water-type Pokemon, etc.).
        :param dupes: Set object storing String representations of Pokemon names; typically Game.dupes object. Set contains Pokemon that are considered "duplicates" and should be excluded, see Area.find_dupe(). 
        :param check_dupes: Boolean flag that represents whether or not to exclude duplicate Pokemon.

        This function is only meant to be used within the Game.distribution() function.

        This function will do the following:
        1) Select daypart based on time value.
        2) Check if type value and power value are valid, if so, set multiplier. multiplier increases the chance of specific Type Pokemon of appearing, and decreases chance of other Type Pokemon of appearing.
        3) Filter out Pokemon in the daypart based on Dupes Clause, and version exclusivity
        4) Calculate float sum of Pokemon values
        5) Calculate each Pokemon's percentage chance of appearing
        6) Print list of Pokemon in descending order of percentage value

        """
        # Choosing all possible wild Pokemon that are present within the day part selected.
        time = v.resolve_daypart(time).lower()
        print(f"{self.name} ({time.capitalize()})")
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
        valid_type = v.valid_type(type)
        
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
        demultiplier = (1-upper_bound)

        # Short lived class for the purpose of the following section
        class Wild:
            def __init__(self, name, percentage, matching_type):
                self.name = name # string value
                self.percentage = percentage # float value
                self.matching_type = matching_type # boolean value

            def sp(self, new_percentage): # stands for set_percentage
                    new_percentage = new_percentage * 10000
                    new_percentage = new_percentage // 1
                    new_percentage = new_percentage / 100
                    self.percentage = new_percentage

        sum = 0.0
        keys = selected.keys()
        allowed_pkmn = []
        for k in keys:
            is_dupe = self.find_dupe(dupes, k.split("_")[0], check_dupes)
            correct_version_ex = v.correct_version(game, k)
            if is_dupe == False and correct_version_ex == True:
                correct_type = (k.find(type) != -1)
                allowed_pkmn.append(Wild(k,0,correct_type))

        for allowed in allowed_pkmn:
            val = 0.0
            if demultiplier != 1 and allowed.matching_type == False: 
                val = selected[allowed.name]*demultiplier
            else:
                val = selected[allowed.name]
            sum = sum + val

        for allowed in allowed_pkmn:
            val = 0.0
            if demultiplier != 1 and allowed.matching_type == False: 
                val = selected[allowed.name]*demultiplier
            else:
                val = selected[allowed.name]
            allowed.sp(val/sum)

        allowed_pkmn = sorted(allowed_pkmn, key=lambda wild: wild.percentage, reverse=True)

        if print_boolean:
            for allowed in allowed_pkmn:
                pkmn_name = allowed.name.split("_")[0]
                print(f"{pkmn_name}: {allowed.percentage}%")
        return allowed_pkmn
            
    def generate(self, game, time, type, power_int, dupes, check_dupes, print_boolean=False):
        """
        Docstring for generate
        
        :param self: Area object.
        :param game: String object representing game, either "Scarlet" or "Violet"
        :param time: String object that represents the daypart, possible values are: "Dawn", "Day", "Dusk", and "Night".
        :param type: String object that represents a Pokemon Type (Grass, Water, etc.).
        :param power: Integer object ranging from 1, 2, or 3; represents an Encounter Power which increases likelihood of a Pokemon of a specific Type (Water-type Pokemon, etc.).
        :param dupes: Set object storing String representations of Pokemon names; typically Game.dupes object. Set contains Pokemon that are considered "duplicates" and should be excluded, see Area.find_dupe(). 
        :param check_dupes: Boolean flag that represents whether or not to exclude duplicate Pokemon.

        This function is only meant to be used within the Game.distribution() function.

        This function will do the following:
        1) Select daypart based on time value.
        2) Check if type value and power value are valid, if so, set multiplier. multiplier increases the chance of specific Type Pokemon of appearing, and decreases chance of other Type Pokemon of appearing.
        3) Filter out Pokemon in the daypart based on Dupes Clause, version exclusivity, and Encounter Power; and create number ranges that will consider a Pokemon "chosen" or "encountered".
        4) Generate a random value, and check which Pokemon was "chosen"/"encountered"
        """
        # Short lived class for the purpose of this function.
        class Range:
            def __init__(self, name, lower, upper):
                self.name = name
                self.lower = lower
                self.upper = upper

            def enclosed(self, number):
                return (self.lower <= number and number <= self.upper)             

        # Select a day part
        time = v.resolve_daypart(time).lower()
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
        valid_type = v.valid_type(type)
        
        # If the type entered is real, then check if the Encounter Power is activated
        power_activated = False
        if valid_type == True:
            power_activated = v.power(power_int)

        
        sum = 0.0
        keys = selected.keys() # Keys are possible wild Pokemon present in the day part selected.
        ranges = []

        for k in keys:
            is_dupe = self.find_dupe(dupes, k.split("_")[0], check_dupes) # Boolean
            correct_version_ex = v.correct_version(game, k) # Boolean
            correct_type = (k.find(type) != -1) # Boolean
            if is_dupe == False and correct_version_ex == True: # Main filter
                if power_activated == True and correct_type == False: # Secondary filter
                    continue
                ranges.append(Range(k, sum, sum + selected[k])) # Otherwise, create ranges with bounds like: [(0, 15.7563), (15.7563, 26.0), etc.]
                sum = sum + selected[k]
        if len(ranges) == 0:
            return [self.name, time.title(), "None"]
        rng = random.uniform(0, sum) # Generate a value
        for r in ranges: # For every range created...
            if r.enclosed(rng): # Proceed if the value falls within the range
                pkmn_name = r.name.split("_")[0]
                return_list = [self.name, time.title(), pkmn_name]
                if print_boolean:
                    print(f"{self.name} ({time.title()}): {pkmn_name}")
                return return_list

    def load_areas():
        """
        Docstring for load_areas

        Static method meant to be used by Game objects.
        Loads the areas, and returns them as a list of dictionaries.
        The dictionaries are numerical and alpha, which take an integer or string respectively.
        """
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
