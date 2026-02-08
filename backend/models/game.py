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
        self.numerical = {}
        
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

    def generate(self, area, time, type, power, check_dupes, print_boolean=False):
        """
        Docstring for generate
        
        :param self: Game object.
        :param area: String or Integer object representing the area.
        :param time: String or Integer object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param power: Integer object related to Encounter Power (Levels 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        """
        pkmn_set = {}
        if isinstance(area, str):
            area = area.strip()
        if isinstance(time, str):
            time = time.strip()
        

        # Making sure that area input is valid
        if isinstance(area, str):
            if area.isnumeric():
                area = int(area)
            if v.valid_area(area) == False:
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
        
        return pkmn_set[area].generate(self.game, daypart, type, power, self.dupes, check_dupes)

    def distribution(self, area, time, type, power, check_dupes, print_boolean=False):
        """
        Docstring for distribution
        
        :param self: Game object.
        :param area: String or Integer object representing the area.
        :param time: String or Integer object representing the daypart.
        :param type: String object representing the Pokemon Type (Grass, Water, etc.).
        :param power: Integer object related to Encounter Power (Levels 1, 2, or 3).
        :param check_dupes: Boolean object that checks whether or not to exclude dupes. Defaults to False later if non-boolean object.
        """
        pkmn_set = {}
        if isinstance(area, str):
            area = area.strip()
        if isinstance(time, str):
            time = time.strip()
        

        # Making sure that area input is valid
        if isinstance(area, str):
            if area.isnumeric():
                area = int(area)
            if v.valid_area(area) == False:
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
        
        return pkmn_set[area].distribution(self.game, daypart, type, power, self.dupes, check_dupes, print_boolean)

    def locate(self, pkmn_to_find, print_boolean):
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
            pkmn_found = any(False if (native_pkmn.strip().lower().split("_")[0].find(pkmn_to_find) == -1) else True for native_pkmn in area.pokemon)
            if pkmn_found == False:
                continue

            # Second, check dayparts.
            # False if area.dawn[native_pkmn] == 0.0 else True
            daypart_found = [False, False, False, False]
            daypart_keys = [area.dawn.keys(), area.day.keys(), area.dusk.keys(), area.night.keys()]
            for x in range(len(daypart_keys)):
                dp = daypart_keys[x]
                for pkmn in dp:
                    name = pkmn.strip().lower().split("_")[0]
                    name = name if (name.find("scarlet") == -1 and name.find("violet") == -1) else name.split(" ")[0]
                    if name == pkmn_to_find:
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
        if print_boolean == True:
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
        duo = Area.load_areas()
        self.numerical = duo[0]
        self.alphabetical = duo[1]

    def print_box(self):
        # Placeholder until it is figured out how to export a text file
        folder = f"data/pokedex"
        file_name = f"box.txt"
        file_path = f"{folder}/{file_name}"

        # Overwriting in case there is pre-existing text
        with open(file_path,"w") as f1:
            f1.write("")

        # Writing each biome and distribution
        with open(file_path, "a") as f1:
            for pkmn in self.box:
                f1.write(f"{pkmn},")
        pass

    def load_box_string(self, string):

    
        # Placeholder until it is figured out how to read an imported text file
        string = string[:len(string)-1]
        pkmns = string.split(",")
        print(len(pkmns))
        pass

    def real_pokemon(self, string):
        return any(string.strip().lower() == pkmn.strip().lower() for pkmn in self.pokedex)