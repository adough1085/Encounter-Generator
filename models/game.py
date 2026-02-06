from models.area import Area
import modules.v as v

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
        
        pkmn_set[area].distribution(self.game, daypart, type, power, self.dupes, check_dupes)

    def locate(self, pkmn_to_find, print_boolean):
        """
        Docstring for locate
        
        :param self: Game object.
        :param pkmn_to_find: String representing name of Pokemon to be found.
        :param print_boolean: Boolean that determines whether to print or not.
        """
        pkmn_to_find = pkmn_to_find.strip().lower()
        areas = self.alphabetical
        habitats = [] # A list is used instead of a set because a set does not print in the same order every time.

        for area in areas.values():
            
            # areas is a dictionary with K: "Area Name", V: Area object.
            # areas.values() represents Area objects, therefore area is an Area object.
            # native_pkmn are String objects representing the Pokemon that can be found in an area's daypart.
            dawn_found = any(native_pkmn.strip().lower().split("_")[0] == pkmn_to_find for native_pkmn in area.dawn.keys())
            day_found = any(native_pkmn.strip().lower().split("_")[0] == pkmn_to_find for native_pkmn in area.day.keys())
            dusk_found = any(native_pkmn.strip().lower().split("_")[0] == pkmn_to_find for native_pkmn in area.dusk.keys())
            night_found = any(native_pkmn.strip().lower().split("_")[0] == pkmn_to_find for native_pkmn in area.night.keys())

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
        duo = Area.load_areas()
        self.numerical = duo[0]
        self.alphabetical = duo[1]
