This program was made for nuzlocking the base game of Pokémon Scarlet and Violet.
A nuzlocke is a type of fanmade challenge in Pokémon games that limits the amount of Pokémon you can capture in a playthrough.
A common rule is that one cannot capture the same Pokémon twice (including evolutionary-related Pokémon).
This program will check:
- the Pokémon that I have already captured
- the chosen area
- time
- boosting power that influences certain types to spawn
and it will either choose a Pokémon or display the probability of each Pokémon based on a weighted score.

There are two classes:
- Game
- Area

The Game class' main role is to:
- keep track of which Pokémon I already have
- keep track of the links, which determine which Pokémon are part of the same evolutionary line