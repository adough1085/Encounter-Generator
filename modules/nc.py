def standard(input):
    # name is some format like "Alfornada Cavern", "alfornada cavern", "aLfORNAda Cavern", etc.
    final_name = ""
    proto_name_arr = input.split(" ")
    for token in proto_name_arr:
        final_name += token.title() + " "
    final_name = final_name[:len(final_name)-1] # Written like "Alfornada Cavern", ensuring that it comes out to the right caps regardless of initial input
    return final_name

def snake_case(input):
    # Meant to standardize names for printing data files
    snake_case_name = ""
    standard_name = standard(input)
    area_name_split=standard_name.lower().split(" ")
    area_name = ""
    for token in area_name_split:
        area_name += token + "_"
    snake_case_name = area_name[:len(area_name)-1]
    return snake_case_name

def image_case(name_input, number):
    # Meant to standardize names to read images and access directory
    image_underscore = standard(name_input).replace(" ", "_")
    i_name = f"{str(number)}Paldea_{image_underscore}"
    return i_name