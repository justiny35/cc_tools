import cc_dat_utils
import json
import cc_data

def make_level_library_from_json(json_data):
    # Initialize new CCDataFile object
    level_library = cc_data.CCDataFile()

    # Loop through json data
    for level_json in json_data["levels"]:
        level = cc_data.CCLevel()
        level.level_number = level_json["level_number"]
        level.time = level_json["time"]
        level.num_chips = level_json["num_chips"]
        level.upper_layer = level_json["upper_layer"]
        level.lower_layer = level_json["lower_layer"]
        # Loop through optional fields
        for field_json in level_json["optional_fields"]:
            if field_json["type"] == "title":
                new_field = cc_data.CCMapTitleField(field_json["title_txt"])
            if field_json["type"] == "hint":
                new_field = cc_data.CCMapHintField(field_json["hint_txt"])
            if field_json["type"] == "password":
                new_field = cc_data.CCEncodedPasswordField(field_json["password_txt"])
            if field_json["type"] == "monsters":
                location = []
                for monster_json in field_json["monster_loc"]:
                    new_location = cc_data.CCCoordinate(monster_json[0], monster_json[1])
                    location.append(new_location)
                new_field = cc_data.CCMonsterMovementField(location)
            level.add_field(new_field)
        level_library.add_level(level)
    return level_library

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

input_json_file = "data/jyook_cc1.json"

with open(input_json_file, "r") as reader:
    level_library_json = json.load(reader)

cc_level_data = make_level_library_from_json(level_library_json)


print(cc_level_data)
cc_dat_utils.write_cc_data_to_dat(cc_level_data, "data/jyook_cc1.dat")
