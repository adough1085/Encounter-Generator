from pathlib import Path
from pixel_count.pixel_count import count_colour_pixels as ccp
import os

class Area:
    def __init__(self, number, name):
        self.number = number # Number corresponds to numbers in image files, which is roughly chronological order in-game
        self.name = name # Written like "Alfornada Cavern"
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
        image_folder = Path("../images/")
        area_folder = image_folder / self.image_name
        biomes_list = ["Bamboo_Forest","Beach","Cave","Desert","Flower","Forest","Lake","Mine","Mountain",
                       "Ocean","Olive","Prairie","Riverside","Rocky_Area","Ruins","Snowfield","Swamp","Town"]
        
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
                pass # Do nothing

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