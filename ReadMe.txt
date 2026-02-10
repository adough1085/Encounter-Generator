This program was made for nuzlocking the base game of Pokémon Scarlet and Violet.
A nuzlocke is a type of fan-made challenge in Pokémon games that has the two core rules:
- you are limited to one Pokémon per unique location
- if a Pokémon you own faints, you cannot use that Pokémon for the rest of the playthrough.

A common optional rule is Dupes Clause, which states:
    - A Pokémon (or its evolutionary-related Pokémon) that you have already captured before are "dupes" or duplicates
    - If encountering a dupe, the dupe can be ignored and you can attempt another encounter
    - This continues until finding a non-dupe

Typically in a nuzlocke, you run into tall grass, and the game will cause a wild Pokémon to attack, and that is your one Pokémon for that unique location.
This is quite different in Pokémon Scarlet and Violet because Pokémon instead spawn in the overworld, and you must physically run into them to start the battle.
There are a few ways to choose your encounter, but most if not all of them have to do with some amount of player choice on where to scout, or the first Pokémon they see. 
None of them are decided mathematically per se, so I made this program.

On Bulbapedia's pages for locations such as West Province (Area One): https://bulbapedia.bulbagarden.net/wiki/West_Province_(Area_One)
List biomes, the Pokémon that spawn in those biomes, as well as the probability weight for 4 parts of the day: Morning, Day, Evening, and Night.
For example, Mankey has a weight of 20 in the Mountain biome of West Province (Area One) for all parts of the day.
In truth, I do not know exactly how the probability weights work.
But I assume it's something like x/sum, where x is the probability weight of the Pokémon for that part of the day, 
and the sum is the total of all probability weight for that part of the day.

Secondly, every location is contained within a reddish-pink border as noted on their Bulbapedia pages.
I combined this with the Biome page: https://bulbapedia.bulbagarden.net/wiki/Biome
which for every biome marks its spawners with purple colouring.
By combining both of these in images, for every location, I could calculate what percentage a certain biome takes up in a location via code to count pixels.
Locations can have any number of different biomes (Riverside, Prairie, Ocean, etc).
The different amounts of square area that biomes cover in a location is different, and therefore is not even.
Hence, it was important to do these calculations as well.

This program does not do any calculations regarding the strong static encounters that you can find in a location.

This program will check:
- the chosen location
- time of day
- boosting power that influences certain types to spawn
- the Pokémon that have already been captured (optional)
and it will either choose a Pokémon or display the probability of each Pokémon based on their probability weights.
Additionally, a Pokémon can be queried and all the locations where it can randomly spawn are listed.

The textbox at the top is where you put the Pokémon you have captured, separated by commas.
For example, "Tauros (Combat Breed), Tauros (Blaze Breed) (Scarlet), Bagon (Violet)". The tag noting version exclusivity is not required.
Alternatively, toggling the checkbox below that will instead only search for the Pokémon in the textbox.
This alternative feature is useful if you have specific set of legal encounters, like, an dogs-only run.

In the logic code, Pokémon is written as Pokemon (without the acute accent, i.e., é) as it is easier to write.
The two main executable files are main.py, and biome_distribution.py. 
main.py is meant to have most of the interactivity.
biome_distribution is meant to generate CSV files that represents the percentage of area that any given biome takes up in a location.

Data Folder contains raw data files in .txt, .csv, or .png form, meant to separate majority of the data from the logic.
Models Folder contains the two main logic classes, Game and Area. Though they are separate classes, they are tightly coupled. 
    The user interacts with Game objects, and the Game class depends on the Area class.