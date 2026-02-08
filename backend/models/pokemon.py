"""
Docstring for models.pokemon
As of right now, this class is unused.
"""

class Pokemon:
    def __init__(self, name, type1, type2, dawn, day, dusk, night):
        dawn = float(dawn)
        day = float(day)
        dusk = float(dusk)
        night = float(night)

        if dawn < 0 or day < 0 or dusk < 0 or night < 0:
            raise Exception("Probability weights cannot be negative.")

        attributes_to_format = [name, type1, type2]
        for attribute in attributes_to_format:
            attribute = attribute.strip().title()
        
        name = name.strip().title()
        type1 = type1.strip().title()
        type2 = type2.strip().title()

        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        t1_valid = type1 in types
        t2_valid = type2 in types

        if t1_valid == False or t2_valid == False:
            raise Exception("Types must be a valid type.")

        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.dawn = dawn
        self.day = day
        self.dusk = dusk
        self.night = night
        self.evolutionary_line = [name]

    # Overload the == operator
    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return (self.name == other.name)
        elif isinstance(other, str):
            return (self.name == other.strip().title())
        else:
            return False
    
    # Overload the in operator
    def __contains__(self, value):
        # Ensure the other operand is also a Pokemon object or String object
        if isinstance(value, Pokemon):
            return any(value.name == pkmn for pkmn in self.evolutionary_line)
        elif isinstance(value, str):
            return any(value.strip().title() == pkmn for pkmn in self.evolutionary_line)
        else:
            return False
    
    def __str__(self):
        return(self.name)
    
    def append_evo(self, value):
        if isinstance(value, Pokemon):
            self.evolutionary_line.append(value.name)
        elif isinstance(value, str):
            self.evolutionary_line.append(value.strip().title())
        else:
            return False