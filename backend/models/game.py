from models.area import Area
from pathlib import Path

class Game:
    def __init__(self, game):
        self.game = game.strip().lower().capitalize()
        self.areas = []
        self.box = []
        self.links = {}
        self.dupes = set()
        
        self.alphabetical = {}
        
        self.define_links()
        self.load_areas()
        
    def define_links(self):
        """
        Docstring for define_links
        
        :param self: Game object.

        This function will read the links.txt, which contain a Pokemon, and the Pokemon it is connected to that are considered "dupes".
        These links will be parsed and added to a dictionary.
        """
        links = ""
        with open(r"data/pokedex/links.txt", "r") as f1:
            links = f1.readlines()
        for line in links:
            pkmn_list = line.strip().split(",")
            header_pkmn = pkmn_list[0]
            linked_pkmn = pkmn_list[1].split("_")
            self.links[header_pkmn] = linked_pkmn

    def populate_dupes(self):
        """
        Docstring for populate_dupes
        
        :param self: Game object.

        For every Pokemon in "the box", search its name in the links dictionary, and add all of those linked Pokemon to the dupes dictionary.
        """
        self.dupes = set()
        for boxed_pkmn in self.box:
            try:
                link = self.links[boxed_pkmn]
            except:
                continue
            for pkmn in link:
                self.dupes.add(pkmn)

    def generate(self, area, daypart, type, encounter_power, check_dupes, specific_pkmn=set(), print_boolean=False):
        """
        Docstring for generate
        
        :param self: Game object.
        :param area: String object representing the area.
        :param daypart: String object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param encounter_power: Integer object related to Encounter Power (Levels 0, 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.
        """
        # Making sure that area, daypart, and type are precleaned before checking validation.
        area = area.strip().title()
        daypart = daypart.strip().title()
        type = type.strip().title()
        if not Game.validate_generate_distribution_input(area, daypart, type, encounter_power):
            print("Generate arguments invalid.")
            return False
        
        return self.alphabetical[area].generate(self.game, daypart, type, encounter_power, self.dupes, check_dupes, specific_pkmn, print_boolean)

    def distribution(self, area, daypart, type, encounter_power, check_dupes, specific_pkmn=set(), print_boolean=False):
        """
        Docstring for distribution
        
        :param self: Game object.
        :param area: String object representing the area.
        :param time: String or Integer object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param encounter_power: Integer object related to Encounter Power (Levels 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.
        """
        # Making sure that area, daypart, and type are precleaned before checking validation.
        area = area.strip().title()
        daypart = daypart.strip().title()
        type = type.strip().title()
        if not Game.validate_generate_distribution_input(area, daypart, type, encounter_power):
            print("Distribution arguments invalid.")
            return False
        
        return self.alphabetical[area].distribution(self.game, daypart, type, encounter_power, self.dupes, check_dupes, specific_pkmn, print_boolean)

    def locate(self, pkmn_to_find, print_boolean=False):
        """
        Docstring for locate
        
        :param self: Game object.
        :param pkmn_to_find: String representing name of Pokemon to be found.
        :param print_boolean: Boolean that determines whether to print or not.

        Given a Pokemon name, every area is quickly checked if the Pokemon is listed to exist.
        If it does, then check every daypart.
        Print the areas and its dayparts that a Pokemon can be found in.
        """

        areas = self.alphabetical
        habitats = [] # A list is used instead of a set because a set does not print in the same order every time.

        for area in areas.values():
            # areas is a dictionary with K: "Area Name", V: Area object.
            # areas.values() represents Area objects, therefore area is an Area object.
            # native_pkmn are String objects representing the Pokemon that can be found in an area or its daypart, in format "Pokemon_Type1_Type2" or "Pokemon (Version)_Type1_Type2"
            # First, immediately rule out areas.

            # String equality is used instead of find because there is currently no logic to transform a diminutive form into a full form.
            # Additionally there are Pokémon with different various such as Tauros (with various Combat, Blaze, and Aqua Breed).
            # Logic to transform a diminutive form into a full form would transform into unintended forms. 

            pkmn_to_find = Game.remove_version_exclusive_tag(pkmn_to_find)
            pkmn_found = any(Game.remove_version_exclusive_tag(native_pkmn.split("_")[0]) == pkmn_to_find for native_pkmn in area.pokemon)
            if pkmn_found == False:
                continue

            # Second, check dayparts.
            # False if area.dawn[native_pkmn] == 0.0 else True
            daypart_found = [False, False, False, False]
            daypart_keys = [area.dawn.keys(), area.day.keys(), area.dusk.keys(), area.night.keys()]
            for x in range(len(daypart_keys)):
                dp = daypart_keys[x]
                daypart_found[x] = any(Game.remove_version_exclusive_tag(native_pkmn.split("_")[0]) == pkmn_to_find for native_pkmn in dp)

            dawn_found = daypart_found[0]
            day_found = daypart_found[1]
            dusk_found = daypart_found[2]
            night_found = daypart_found[3]

            # If a Pokemon are found in every daypart, then simply the Area is named.
            if dawn_found and day_found and dusk_found and night_found:
                habitats.append(area.name)
            # If a Pokemon is only found in specific dayparts, then it will list which Area and dayparts it can be found in.
            elif dawn_found or day_found or dusk_found or night_found:
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
            else:
                pass # Pokemon was not found in this Area.

        # If the print boolean is flagged True, then print
        if print_boolean:
            if len(habitats) >= 1:
                print(f"{pkmn_to_find} is located in:")
                for x in habitats:
                    print(f"- {x}")
            else:
                print(f"{pkmn_to_find} not found as a random encounter.")
        
        # Return list of Areas that it can be found in.
        return habitats

    def load_areas(self):
        """
        Docstring for load_areas
        
        :param self: Game object.

        Loads all areas.
        """
        areas = Area.load_areas()
        self.alphabetical = areas

    def validate_pokemon(self, pkmn_name):
        pokedex = list(map(lambda x: Game.remove_version_exclusive_tag(x.split(",")[0]), self.links))
        return any(Game.remove_version_exclusive_tag(pkmn_name) == pkmn for pkmn in pokedex)
    
    def validate_generate_distribution_input(area: str, daypart: str, type: str, power: int):
        """
        Docstring for validate_gen_dis_input
        All string inputs are expected to have been precleaned with strip() and title() prior to being passed into function.
        :param area: String object representing area.
        :param daypart: String object representing daypart.
        :param type: String object representing Pokémon Type.
        :param power: String object representing power.
        :param check_dupes: Boolean object representing whether or not to remove duplicate (and evolutionary relatives) from Pokémon to generate or calculate distributions for.
        """
        if not Area.validate_area(area):
            print("Invalid Area")
            return False
        
        if not Area.validate_daypart(daypart):
            print("Invalid Daypart")
            return False
        
        if not Area.validate_type(type): # While an optional feature, it should be ensured the value is at least correct for later processes. 
            print("Invalid Type")
            return False

        if not (0 <= power or power <= 3): # While an optional feature, it should be ensured the value is at least correct for later processes. 
            print("Invalid Power")
            return False

        # Else if all checks are passed, return True
        return True

    def process_generate_request(self, global_text: str, area: str, daypart: str, pkmn_type: str, encounter_power_level: int, dupes_clause_enabled: bool, specific_pkmn_set_enabled: bool, print_enabled: bool):
        """
        Docstring for process_generate_request
        
        :param self: Game object.
        :param global_text: String object meant to represent the Pokémon that the user owns; if specific_pkmn_set_enabled is True, then it represents the specific kind of Pokémon to include.
        :param area: String object that is the area name.
        :param daypart: String object that represents the time of day.
        :param pkmn_type: String object that represents the specific Pokémon Type that the Encounter Power will force more Pokémon of the same type to spawn.
        :param encounter_power_level: String object at that represents Encounter Power Level ranging from 0 to 3.
        :param dupes_clause_enabled: Boolean object that represents whether or not Dupes Clause is to be used.
        :param specific_pkmn_set_enabled: Boolean object that represents whether or not a specific subset of Pokémon are to be used instead of all of the Pokémon in an area and time.
        :param print_enabled: Boolean object that represents whether or not to print the result in the console.
        """
        self.box = []
        pkmn_list = global_text.split(",")
        pkmn_list = list(map(lambda x: x.strip(), pkmn_list))
        pkmn_list = list(map(lambda x: Area.add_version_exclusive_tag(x) if self.validate_pokemon(x) else False, pkmn_list)) # Checks Pokemon name, filters out fake names, add tag if applicable
        pkmn_list = [pkmn for pkmn in pkmn_list if pkmn] # Filters out False
        
        if dupes_clause_enabled:
            self.populate_dupes()

        subset = set()
        if specific_pkmn_set_enabled:
            subset = set(self.box)
    
        return self.generate(area, daypart, pkmn_type, encounter_power_level, self.dupes, subset, print_enabled)
    
    def process_distribution_request(self, global_text: str, area: str, daypart: str, pkmn_type: str, encounter_power_level: int, dupes_clause_enabled: bool, specific_pkmn_set_enabled: bool, print_enabled: bool):
        """
        Docstring for process_distribution_request
        
        :param self: Game object.
        :param global_text: String object meant to represent the Pokémon that the user owns; if specific_pkmn_set_enabled is True, then it represents the specific kind of Pokémon to include.
        :param area: String object that is the area name.
        :param daypart: String object that represents the time of day.
        :param pkmn_type: String object that represents the specific Pokémon Type that the Encounter Power will force more Pokémon of the same type to spawn.
        :param encounter_power_level: String object at that represents Encounter Power Level ranging from 0 to 3.
        :param dupes_clause_enabled: Boolean object that represents whether or not Dupes Clause is to be used.
        :param specific_pkmn_set_enabled: Boolean object that represents whether or not a specific subset of Pokémon are to be used instead of all of the Pokémon in an area and time.
        :param print_enabled: Boolean object that represents whether or not to print the result in the console.
        """
        self.box = []
        pkmn_list = global_text.split(",")
        pkmn_list = list(map(lambda x: x.strip(), pkmn_list))
        pkmn_list = list(map(lambda x: Area.add_version_exclusive_tag(x) if self.validate_pokemon(x) else False, pkmn_list)) # Checks Pokemon name, filters out fake names, add tag if applicable
        pkmn_list = [pkmn for pkmn in pkmn_list if pkmn] # Filters out False
        
        if dupes_clause_enabled:
            self.populate_dupes()

        subset = set()
        if specific_pkmn_set_enabled:
            subset = set(self.box)
    
        return self.distribution(area, daypart, pkmn_type, encounter_power_level, self.dupes, subset, print_enabled)
    
    def add_version_exclusive_tag(pkmn_name: str):
        return Area.add_version_exclusive_tag(pkmn_name)
    
    def remove_version_exclusive_tag(pkmn_name: str):
        return Area.remove_version_exclusive_tag(pkmn_name)