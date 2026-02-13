import random
from modules import nc as nc

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
           
    def generate(self, game: str, daypart: str, type: str , encounter_power: int, dupes: set, check_dupes: bool, specific_pkmn: set, print_boolean: bool):
        """
        Docstring for generate
        
        :param self: Area object.
        :param game: String object representing game version, possible values are: "Scarlet" or "Violet"
        :param daypart: Precleaned string object that represents the daypart, possible values are: "Dawn", "Day", "Dusk", and "Night".
        :param type: String object that represents a Pokemon Type, possible values are "Grass", "Water", etc.
        :param encounter_power: Integer object ranging from 0, 1, 2, or 3; represents an Encounter Power which increases likelihood of a Pokemon of a specific Type (Water-type Pokemon, etc.).
        :param dupes: Set object storing String representations of Pokemon names; typically Game.dupes object. Set contains Pokemon that are considered "duplicates" and should be excluded, see Area.find_dupe(). 
        :param check_dupes: Boolean flag that represents whether or not to exclude duplicate Pokemon.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.
        

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
        daypart_selected = {}
        if daypart == "Dawn":
            daypart_selected = self.dawn
        elif daypart == "Day":
            daypart_selected = self.day
        elif daypart == "Dusk":
            daypart_selected = self.dusk
        elif daypart == "Night":
            daypart_selected = self.night
        
        # Use random number generator to decide if Encounter Power is activated
        encounter_power_activated = Area.activate_encounter_power(encounter_power)
        
        sum = 0.0
        pkmn_keys = daypart_selected.keys() # Keys are possible wild Pokemon present in the daypart selected.
        ranges = []

        # Normal operations, do not calculate for specific Pokemon only 
        if len(specific_pkmn) == 0:
            for key in pkmn_keys:
                is_dupe = self.find_dupe(dupes, key.split("_")[0], check_dupes) # Boolean
                correct_version_exclusive = Area.validate_compatible_version(game, key) # Boolean
                correct_type = (key.find(type) != -1) # Boolean

                # Check if Pokémon is not considered a duplicate, and that the Pokémon is compatible with the game version; if not, continue to next Pokémon
                if not (not is_dupe and correct_version_exclusive):
                    continue

                # Check if an Encounter Power was activated, and if the Pokémon is not of the specified type; if so, continue to next Pokémon
                if encounter_power_activated and not correct_type: # Second filter
                    continue

                # If those filters are passed, create ranges with bounds like: [(0, 15.7563), (15.7563, 26.0), etc.]
                ranges.append(Range(key, sum, sum + daypart_selected[key])) 
                sum = sum + daypart_selected[key]
        
        # If length of specific_pkmn is greater than 0, then calculate for specific Pokemon only
        # No need to check for dupes, as this specific Pokemon set is already filtering out Pokemon
        if len(specific_pkmn) > 0: 
            for key in pkmn_keys:
                correct_version_exclusive = Area.validate_compatible_version(game, key) # Boolean
                correct_type = (key.find(type) != -1) # Boolean
                contained_in_specific_subset = any(False if key.strip().lower().find(subset_pkmn.strip().lower()) == -1 else True for subset_pkmn in specific_pkmn) # Boolean

                # Check if Pokémon is compatible with game's version, and check if Pokémon is in specific subset; if not, immediately go to next Pokémon
                if not (correct_version_exclusive and contained_in_specific_subset): 
                    continue

                # Check if Encounter Power is active, and check if Pokémon is not the specific type; if so, immediately go to next Pokémon
                if encounter_power_activated and not correct_type:
                    continue
        
                # Otherwise, create ranges with bounds like: [(0, 15.7563), (15.7563, 26.0), etc.]
                ranges.append(Range(key, sum, sum + daypart_selected[key])) 
                sum = sum + daypart_selected[key]


        # If no Pokémon are eligible due to a combination of Dupes Clause and Encounter Power for example, return that for the Area, Daypart, no Pokémon were selected.
        if len(ranges) == 0:
            return [self.name, daypart, "None"]
        
        # Otherwise, generate a Pokémon
        rng = random.uniform(0, sum) # Generate a value
        for r in ranges: # For every range created...; r is used because range in Python is defined to have functionality.
            if r.enclosed(rng): # Proceed if the value falls within the range
                pkmn_name = r.name.split("_")[0]
                if print_boolean:
                    print(f"{self.name} ({daypart}): {pkmn_name}")
                return [self.name, daypart, pkmn_name]

    def distribution(self, game: str, daypart: str, type: str, encounter_power: int, dupes: set, check_dupes: bool, specific_pkmn: set, print_boolean: bool):
        """
        Docstring for distribution
        
        :param self: Area object.
        :param game: String object representing game, either "Scarlet" or "Violet".
        :param daypart: Precleaned string object that represents the daypart, possible values are: "Dawn", "Day", "Dusk", and "Night".
        :param type: String object that represents a Pokemon Type, possible values are "Grass", "Water", etc.
        :param encounter_power: Integer object ranging from 0, 1, 2, or 3; represents an Encounter Power which increases likelihood of a Pokemon of a specific Type (Water-type Pokemon, etc.).
        :param dupes: Set object storing String representations of Pokemon names; typically Game.dupes object. Set contains Pokemon that are considered "duplicates" and should be excluded, see Area.find_dupe(). 
        :param check_dupes: Boolean flag that represents whether or not to exclude duplicate Pokemon.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.

        This function is only meant to be used within the Game.distribution() function.

        This function will do the following:
        1) Select daypart based on time value.
        2) Check if type value and power value are valid, if so, set multiplier. multiplier increases the chance of specific Type Pokemon of appearing, and decreases chance of other Type Pokemon of appearing.
        3a) Filter out Pokemon in the daypart based on Dupes Clause, and version exclusivity, these is what normally happens
        3b) If specific_pkmn is a
        4) Calculate float sum of Pokemon values
        5) Calculate each Pokemon's percentage chance of appearing
        6) Print list of Pokemon in descending order of percentage value

        """
        # Choosing all possible wild Pokemon that are present within the daypart selected.
        daypart_selected = {}
        if daypart == "Dawn":
            daypart_selected = self.dawn
        elif daypart == "Day":
            daypart_selected = self.day
        elif daypart == "Dusk":
            daypart_selected = self.dusk
        elif daypart == "Night":
            daypart_selected = self.night

        """
        I am under the assumption that the way Encounter Powers works is: 
        whatever % of encounters will be the enforced type, while the other % will always be a different type.
        I have yet to find extensive evidence that proves or disproves this, but it is a simpler assumption
        compared to the possibility that the other % still having a chance to spawn the enforced type.
        """
        upper_bound = 0
        if encounter_power == 1:
            upper_bound = 0.50
        elif encounter_power == 2:
            upper_bound = 0.75
        elif encounter_power == 3: 
            upper_bound = 1
        demultiplier = (1-upper_bound) # demultipler will be used to reduce likelihood of Pokémon that do not match the specified type when an Encounter Power is active.

        # Short lived class for the purpose of the following section
        class Wild:
            def __init__(self, name: str, percentage: float, matching_type: bool):
                """
                Docstring for __init__
                
                :param self: Description
                :param name: String value representing Pokémon name.
                :param percentage: Float value representing percentage chance that a Pokémon could be chosen.
                :param matching_type: Boolean value representing whether or not the Pokémon matches the specified type.
                """
                self.name = name
                self.percentage = percentage
                self.truncated_percentage = 0.0
                self.matching_type = matching_type

            def set_percentage(self, new_percentage: float):
                    self.percentage = new_percentage 
                    new_percentage = new_percentage * 10000 # Multiplying to 5 whole digits
                    new_percentage = new_percentage // 1 # Truncating
                    new_percentage = new_percentage / 100 # Dividing down to 5 decimal places
                    self.truncated_percentage = new_percentage
                


        # Filter the Pokémon to calculate for based on Dupes Clause, version exclusivity, Encounter Power, and whether a specific subset was called for.
        pkmn_keys = daypart_selected.keys()
        allowed_pkmn = []

        # Normal operations, do not calculate for specific Pokemon only 
        if len(specific_pkmn) == 0:
            for key in pkmn_keys:
                is_dupe = self.find_dupe(dupes, key.split("_")[0], check_dupes)
                correct_version_exclusive = Area.validate_compatible_version(game, key)

                if is_dupe == False and correct_version_exclusive == True:
                    correct_type = (key.find(type) != -1) # Check if Pokemon is equal to Encounter Power type
                    allowed_pkmn.append(Wild(key, 0.0, correct_type))
        
        # If length of specific_pkmn is greater than 0, then calculate for specific Pokemon only
        # No need to check for dupes, as this specific Pokemon set is already filtering out Pokemon
        if len(specific_pkmn) > 0: 
            for key in pkmn_keys:
                contained_in_specific_subset = any(False if key.strip().lower().find(subset_pkmn.strip().lower()) == -1 else True for subset_pkmn in specific_pkmn)
                correct_version_exclusive = Area.validate_compatible_version(game, key)

                if correct_version_exclusive and contained_in_specific_subset:
                    correct_type = (key.find(type) != -1) # Check if Pokemon is equal to Encounter Power type
                    allowed_pkmn.append(Wild(key, 0.0, correct_type))

        

        # First, calculate sum of all probability weight
        sum = 0.0
        for allowed in allowed_pkmn:
            val = 0.0
            if demultiplier != 1 and not allowed.matching_type: # If Encounter Power is active and Pokémon does not match specified type
                val = daypart_selected[allowed.name]*demultiplier
            else:
                val = daypart_selected[allowed.name]
            sum = sum + val

        # Second, calculate each Pokémon
        for allowed in allowed_pkmn:
            val = 0.0
            if demultiplier != 1 and not allowed.matching_type: # If Encounter Power is active and Pokémon does not match specified type
                val = daypart_selected[allowed.name]*demultiplier
            else:
                val = daypart_selected[allowed.name]

            if (sum == 0.0): # Prevents division by 0
                allowed.percentage = 0.0
            else:
                allowed.set_percentage(val/sum)

        # Third, filter out Pokémon where the percentage is 0.0, not much reason to show Pokémon if you cannot catch them under set of parameters
        allowed_pkmn = list(map(lambda pkmn: pkmn if pkmn.percentage > 0.0 else False, allowed_pkmn))
        allowed_pkmn = [pkmn for pkmn in allowed_pkmn if pkmn] # Filters out False

        # Sort based on percentage values starting from largest to smallest
        allowed_pkmn = sorted(allowed_pkmn, key=lambda pkmn: pkmn.percentage, reverse=True)

        if print_boolean:
            for allowed in allowed_pkmn:
                pkmn_name = allowed.name.split("_")[0]
                print(f"{pkmn_name}: {allowed.percentage}%")
        return allowed_pkmn # list object
 
    def load_areas():
        """
        Docstring for load_areas

        Static method meant to be used by Game objects.
        Loads the areas, and returns them as a dictionary.
        The areas in the dictionary are listed in alphabetical order.
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
        alpha["Great Crater Of Paldea"] = great_crater_of_paldea
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
        
        return alpha

    def validate_compatible_version(game_string, pkmn_to_check):
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

    def activate_encounter_power(encounter_power_number):
        """
        Docstring for power_int
        
        :param self: Area object.
        :param power_int: An Integer intended to 1, 2, or 3. Depending on power_int level, it has a greater chance of forcing a specific Type (Grass, Water, etc.) Pokemon to spawn.
        
        upper_bound represents the percentage chance that a specific Type Pokemon is forced to spawn.
        Generates a random number from 1 to 100 (inclusive), if it is less than or equal to the upper_bound, then the specific Type is forced.
        """
        upper_bound = 0
        if encounter_power_number == 1:
            upper_bound = 50
        elif encounter_power_number == 2:
            upper_bound = 75
        elif encounter_power_number == 3: 
            upper_bound = 100
        else:
            return False
        
        return random.randint(1,100) <= upper_bound
    
    def add_version_exclusive_tag(pkmn_name: str):
        pokedex = list()
        with open(r"data/pokedex/links.txt","r") as f1:
            lines = f1.readlines()
        pokedex = list(map(lambda x: x.split(",")[0], lines))

        for pkmn in pokedex:
            pkmn_full_name = pkmn.split("_")[0]
            if pkmn.find("Scarlet") != -1 or pkmn.find("Violet") != -1:
                if Area.remove_version_exclusive_tag(pkmn_full_name) == Area.remove_version_exclusive_tag(pkmn_name):
                    return pkmn_full_name

    def remove_version_exclusive_tag(pkmn_name: str):
        """
        Docstring for remove_version_exclusive_tag
        
        :param pkmn_name: String object that represents the Pokémon's name; should be in a form such as "Deino (Scarlet)"

        This function will transform a value such as "Deino (Scarlet)" to "Deino".
        Otherwise, it will return a value such as "Deino", "Bagon", "Pikachu", "Whateverinputisenteredbecausethisdoesnotcheckpokemonname"
        """
        pkmn_name = pkmn_name.strip().lower()
        if pkmn_name.find("scarlet") != -1 or pkmn_name.find("violet") != -1:
            pkmn_name = pkmn_name.replace("(scarlet)", " ")
            pkmn_name = pkmn_name.replace("(violet)", " ")
            pkmn_name = pkmn_name.strip()
        return pkmn_name.title() # Converts something like Deino 
    
    def validate_area(area_name):
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

        return any(area_name.lower() == area.lower() for area in areas)
    
    def validate_type(type_input):
        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        return any(type_input.strip().title() == pkmn_type for pkmn_type in types)

    def validate_daypart(daypart_name: str):
            """
            Docstring for validate_daypart

            :param daypart_input: String object that is expected to be cleaned by strip() and title().
            """
            valid_dayparts = {"Dawn", "Day", "Dusk", "Night"}
            valid = any(daypart_name == valid_daypart for valid_daypart in valid_dayparts)
            return valid

