def valid_area(string_input):
        areas = {
        "Alfornada Cavern",
        "Asado Desert",
        "Cabo Poco",
        "Casseroya Lake",
        "Dalizapa Passage",
        "East Paldean Sea",
        "East Province (Area One)",
        "East Province (Area Two)",
        "East Province (Area Three)",
        "Glaseado Mountain",
        "Great Crater of Paldea",
        "Inlet Grotto",
        "North Paldean Sea",
        "North Province (Area One)",
        "North Province (Area Two)",
        "North Province (Area Three)",
        "Poco Path",
        "Pokemon League",
        "Socarrat Trail",
        "South Paldean Sea",
        "South Province (Area One)",
        "South Province (Area Two)",
        "South Province (Area Three)",
        "South Province (Area Four)",
        "South Province (Area Five)",
        "South Province (Area Six)",
        "Tagtree Thicket",
        "West Paldean Sea",
        "West Province (Area One)",
        "West Province (Area Two)",
        "West Province (Area Three)"
        }

        return any(string_input.lower() == area.lower() for area in areas)

def resolve_daypart(time):
        valid = True
        valid_dayparts = {"Dawn", "Day", "Dusk", "Night"}
        daypart = ""

        if isinstance(time, str):
            time = time.title()
            for dp in valid_dayparts:
                if time == dp:
                    daypart = dp
                    break
            valid = False

        if isinstance(time, int):
            if time == 0:
                daypart = "Dawn"
            elif time == 1:
                daypart = "Day"
            elif time == 2:
                daypart = "Dusk"
            elif time == 3:
                daypart = "Night"
            else:
                valid = False

        if valid == False:
            return False
        else:
            return daypart
