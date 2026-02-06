from pathlib import Path
from modules.pc import count_colour_pixels as ccp
import modules.nc as nc

class Area:
    """
    Docstring for Area

    This program is not meant to always run, it will only run if the area-biome distributions must be reprinted.
    """
    def __init__(self, number, name):
        self.number = number # Number corresponds to numbers in image files, which is roughly chronological order in-game
        self.name = nc.standard(name)
        self.snake_case_name = nc.snake_case(name)
        self.image_name = nc.image_case(name, number)
        self.biomes = []
        self.biome_pixels = {}
        self.distribution = {}
        self.pixel_total = 0
        self.target_colour_rgb = (80, 47, 121) # Purple sort of colour

        
    def count(self):
        """
        Docstring for count
        
        :param self: Area object.

        This function will use image files that are named in the following format: "<n>Paldea_<Area_Name>_Map_<Biome>.png" where:
            - n is an integer from 1 to 31, which notes in roughly chronological order where areas would be visited
            - Area_Name is the name of the area in Pascal Case with underscores (_) as a word separator
            - Biome is the name of the biome type
        The word "Map" is used as a separator between Area_Name and Biome.
        Within an image file, purple pixels mark square area which the biome covers.

        For every area, rather than hard-coding which biomes will be loading, every area will check if it contains every biome.
        If a biome exists and is not yet recorded, it is added to self.biome. If a biome does not exist, a counter is incremented by 1.
        For every biome in self.biome, its respective image file is opened, the purple pixels are counted and that number is recorded and added to sum of total pixels.
        
        If for an area no biomes are found, then there are no biome image files for the area.
        These are special cases, which within the base game are two areas:
        - Cabo Poco, where you simply choose your first ever Pokemon in a playthrough
        - Great Crater of Paldea, a mysterious area where visual map data is not included (and datamined images of biome coverage are not publicly available)
        In these cases, there is no influence from biome size, and the calculated distribution is almost certainly different from what is true within the game.
        """
        # For every biome, check if it exists in the region
        image_folder = "data/image"
        area_folder = f"{image_folder}/{self.image_name}"
        biomes_list = ["Bamboo_Forest","Beach","Cave","Desert","Flower","Forest","Lake","Mine","Mountain",
                       "Ocean","Olive","Prairie","Riverside","Rocky_Area","Ruins","Snowfield","Swamp","Town"]
        missing_biome_count = 0
        
        for biome in biomes_list:
            file_name = f"{self.image_name}_Map_{biome}.png"
            file_path = f"{area_folder}/{file_name}"
            # Test if the region exists, if yes, add biome to existing biomes in region, and count pixels.
            try:
                with open(file_path, 'r') as f:
                    pass # Don't actually need to try reading anything; this is to check if the file exists
                biome_name = biome.replace("_", " ")
                if biome_name not in self.biomes:
                    self.biomes.append(biome_name)
                    b_pixels = ccp(file_path, self.target_colour_rgb)
                    self.biome_pixels[biome_name] = b_pixels
                    self.pixel_total += b_pixels
            except FileNotFoundError:
                missing_biome_count += 1
        
        # If none of the traditional biomes are present, create a special biome.
        # Only applies to Cabo Poco and Great Crater of Paldea.
        if missing_biome_count == len(biomes_list):
            biome_name = "Special"
            self.biomes.append(biome_name)
            self.biome_pixels[biome_name] = 100
            self.pixel_total += 100

    def calculate_distribution(self):
        """
        Docstring for calculate_distribution
        
        :param self: Area object.

        For every biome, access their pixels within the biome_pixels dictionary and compare it to pixel_total.
        Write the percentage within the distribution dictionary.
        """
        for biome in self.biomes:
            percentage = self.biome_pixels[biome] / self.pixel_total
            self.distribution[biome] = percentage

    def csv(self):
        """
        Docstring for csv
        
        :param self: Area object.

        Creates a CSV file named for example "alfornada_cavern.csv" that contains headers: "Biome", and "Percentage".
        Biome represents the biome name/type.
        Percentage represents what percent the particular biome covers in comparison to all covered biome space.
        """
        subdirectory_path = Path("data/distribution")
        file_name = self.snake_case_name + ".csv"
        file_path = subdirectory_path / file_name
        subdirectory_path.mkdir(parents=True, exist_ok=True)

        # Overwriting in case there is pre-existing text
        with open(file_path,"w") as f1:
            f1.write("Biome,Percentage\n")

        # Writing each biome and distribution
        with open(file_path, "a") as f1:
            for biome in self.biomes:
                line = f"{biome},{self.distribution[biome]}\n"
                f1.write(line)

    def run(self):
        """
        Docstring for run
        
        :param self: Area object.

        Executes count, calculate_distribution, and csv methods for this area.
        """
        self.count()
        self.calculate_distribution()
        self.csv()

list = []
cabo_poco = Area(1, "Cabo Poco")
poco_path = Area(2, "Poco Path")
inlet_grotto = Area(3, "Inlet Grotto")
south_province_area_one = Area(4, "South Province (Area One)")
south_province_area_two = Area(5, "South Province (Area Two)")
south_province_area_three = Area(6, "South Province (Area Three)")
west_province_area_one = Area(7, "West Province (Area One)")
south_paldean_sea = Area(8, "South Paldean Sea")
south_province_area_four = Area(9, "South Province (Area Four)")
south_province_area_five = Area(10, "South Province (Area Five)")
east_province_area_one = Area(11, "East Province (Area One)")
east_province_area_two = Area(12, "East Province (Area Two)")
east_province_area_three = Area(13, "East Province (Area Three)")
west_province_area_two = Area(14, "West Province (Area Two)")
tagtree_thicket = Area(15, "Tagtree Thicket")
west_province_area_three = Area(16, "West Province (Area Three)")
east_paldean_sea = Area(17, "East Paldean Sea")
west_paldean_sea = Area(18, "West Paldean Sea")
glaseado_mountain = Area(19, "Glaseado Mountain")
alfornada_cavern = Area(20, "Alfornada Cavern")
south_province_area_six = Area(21, "South Province (Area Six)")
asado_desert = Area(22, "Asado Desert")
north_province_area_three = Area(23, "North Province (Area Three)")
north_province_area_two = Area(24, "North Province (Area Two)")
north_province_area_one = Area(25, "North Province (Area One)")
north_paldean_sea = Area(26, "North Paldean Sea")
casseroya_lake = Area(27, "Casseroya Lake")
socarrat_trail = Area(28, "Socarrat Trail")
dalizapa_passage = Area(29, "Dalizapa Passage")
pokemon_league = Area(30, "Pokemon League")
great_crater_of_paldea = Area(31, "Great Crater of Paldea")

list.append(cabo_poco)
list.append(poco_path)
list.append(inlet_grotto)
list.append(south_province_area_one)
list.append(south_province_area_two)
list.append(south_province_area_three)
list.append(west_province_area_one)
list.append(south_paldean_sea)
list.append(south_province_area_four)
list.append(south_province_area_five)
list.append(east_province_area_one)
list.append(east_province_area_two)
list.append(east_province_area_three)
list.append(west_province_area_two)
list.append(tagtree_thicket)
list.append(west_province_area_three)
list.append(east_paldean_sea)
list.append(west_paldean_sea)
list.append(glaseado_mountain)
list.append(alfornada_cavern)
list.append(south_province_area_six)
list.append(asado_desert)
list.append(north_province_area_three)
list.append(north_province_area_two)
list.append(north_province_area_one)
list.append(north_paldean_sea)
list.append(casseroya_lake)
list.append(socarrat_trail)
list.append(dalizapa_passage)
list.append(pokemon_league)
list.append(great_crater_of_paldea)

"""
for area in list:
    area.run()
"""