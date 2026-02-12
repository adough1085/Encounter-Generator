from models.area import Area
import modules.v as v
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
        for boxed_pkmn in self.box:
            try:
                link = self.links[boxed_pkmn]
            except:
                continue
            for pkmn in link:
                self.dupes.add(pkmn)

    def generate(self, area, daypart, type, power, check_dupes, specific_pkmn=set(), print_boolean=False):
        """
        Docstring for generate
        
        :param self: Game object.
        :param area: String object representing the area.
        :param daypart: String object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param power: Integer object related to Encounter Power (Levels 0, 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.
        """
        # Making sure that area, daypart, and type are precleaned before checking validation.
        area = area.strip().title()
        daypart = daypart.strip().title()
        type = type.strip().title()
        if not Game.validate_gen_dis_input(area, daypart, type, power, check_dupes):
            print("Generate arguments invalid.")
            return False
        
        return self.alphabetical[area].generate(self.game, daypart, type, power, self.dupes, check_dupes, specific_pkmn, print_boolean)

    def distribution(self, area, daypart, type, power, check_dupes, specific_pkmn=set(), print_boolean=False):
        """
        Docstring for distribution
        
        :param self: Game object.
        :param area: String object representing the area.
        :param time: String or Integer object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param power: Integer object related to Encounter Power (Levels 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        :param specific_pkmn: Set object that if greater than one signifies that instead of calculating for all Pokemon in an area, only calculate for the ones in the set. Ignores check_dupes if non-empty set.
        :param print_boolean: Boolean object that checks whether or not to print.
        """
        # Making sure that area, daypart, and type are precleaned before checking validation.
        area = area.strip().title()
        daypart = daypart.strip().title()
        type = type.strip().title()
        if not Game.validate_gen_dis_input(area, daypart, type, power, check_dupes):
            print("Distribution arguments invalid.")
            return False
        
        return self.alphabetical[area].distribution(self.game, daypart, type, power, self.dupes, check_dupes, specific_pkmn, print_boolean)

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
        pkmn_to_find = pkmn_to_find.strip().lower()
        areas = self.alphabetical
        habitats = [] # A list is used instead of a set because a set does not print in the same order every time.

        for area in areas.values():
            # areas is a dictionary with K: "Area Name", V: Area object.
            # areas.values() represents Area objects, therefore area is an Area object.
            # native_pkmn are String objects representing the Pokemon that can be found in an area or its dayparts.
            # First, immediately rule out areas.

            # This immensely long logic is broken down as follows:
            # a) The Find function searches a string for a substring, and returns -1 if False. Find is more inclusive than the equality operator.
            # b) The Ternary Statement is similar to an if statement
            # c) Any statement allows for modification of an iteratable's values, and evaluates to False if all values are False, empty, or 0, otherwise True.

            pkmn_found = any(v.remove_version_exclusive_tag(native_pkmn.strip().lower().split("_")[0]).lower() == v.remove_version_exclusive_tag(pkmn_to_find).lower() for native_pkmn in area.pokemon)
            if pkmn_found == False:
                continue

            # Second, check dayparts.
            # False if area.dawn[native_pkmn] == 0.0 else True
            daypart_found = [False, False, False, False]
            daypart_keys = [area.dawn.keys(), area.day.keys(), area.dusk.keys(), area.night.keys()]
            for x in range(len(daypart_keys)):
                dp = daypart_keys[x]
                for pkmn in dp:
                    # pkmn format = "Bronzong_Steel_Psychic"
                    name = pkmn.strip().lower().split("_")[0]
                    refactored_native = v.remove_version_exclusive_tag(name).lower()
                    refactored_pkmn_to_find = v.remove_version_exclusive_tag(pkmn_to_find).lower()

                    if refactored_native == refactored_pkmn_to_find:
                        daypart_found[x] = True
                        break

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
        pkmn_to_find = pkmn_to_find.title()
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

    def validate_gen_dis_input(area: str, daypart: str, type: str, power: int, check_dupes: bool):
        """
        Docstring for validate_gen_dis_input
        All string inputs are expected to have been precleaned with strip() and title() prior to being passed into function.
        :param area: String object representing area.
        :param daypart: String object representing daypart.
        :param type: String object representing Pokémon Type.
        :param power: String object representing power.
        :param check_dupes: Boolean object representing whether or not to remove duplicate (and evolutionary relatives) from Pokémon to generate or calculate distributions for.
        """
        if not v.valid_area(area):
            print("Invalid Area")
            return False
        
        if not v.validate_daypart(daypart):
            print("Invalid Daypart")
            return False
        
        if not v.valid_type(type): # Does not return False and stop program as this is an optional feature.
            print("Invalid Type")

        if power > 0 or power < 3: # Does not return False and stop program as this is an optional feature.
            print("Invalid Power")

        # No check required for check_dupes, expected bool data type should already prevent invalid entry.
        # If all conditions at least area and daypart are valid, then return True and allow program to proceed.
        return True

    def real_pokemon(string):
        return v.valid_pokemon(string)