from pathlib import Path
from pixel_count.pc import count_colour_pixels as ccp

class Area:
    def __init__(self, number, name):
        self.number = number # Number corresponds to numbers in image files, which is roughly chronological order in-game
        self.name = ""
        proto_name_arr = name.split(" ")
        for token in proto_name_arr:
            self.name += token.title() + " "
        self.name = self.name[:len(self.name)-1] # Written like "Alfornada Cavern", ensuring that it comes out to the right caps regardless of initial input
        self.snake_case_name = "" # Written like "alfornada_cavern"
        self.image_name = ""
        self.biomes = []
        self.biome_pixels = {}
        self.distribution = {}
        self.pixel_total = 0
        self.target_colour_rgb = (80, 47, 121)

        area_name_split=self.name.lower().split(" ")
        area_name = ""
        for token in area_name_split:
            area_name += token + "_"
        self.snake_case_name = area_name[:len(area_name)-1]

        name_pascal_underscore = self.name.replace(" ", "_")
        i_name = f"{str(self.number)}Paldea_{name_pascal_underscore}"
        self.image_name = i_name

        
    def count(self):
        # For every biome, check if it exists in the region
        image_folder = Path("data/image/")
        area_folder = image_folder / self.image_name
        biomes_list = ["Bamboo_Forest","Beach","Cave","Desert","Flower","Forest","Lake","Mine","Mountain",
                       "Ocean","Olive","Prairie","Riverside","Rocky_Area","Ruins","Snowfield","Swamp","Town"]
        missing_biome_count = 0
        
        for biome in biomes_list:
            file_name = f"{area_folder}_Map_{biome}.png"
            file_path = area_folder / file_name
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
        # For every biome, access their pixels within the biome_pixels dictionary and compare it to pixel_total.
        # Write the percentage within the distribution dictionary.
        for biome in self.biomes:
            percentage = self.biome_pixels[biome] / self.pixel_total
            self.distribution[biome] = percentage

    def csv(self):
        subdirectory_path = Path("distributions")
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

for area in list:
    area.run()