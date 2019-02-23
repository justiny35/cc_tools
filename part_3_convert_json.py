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
        level.optional_fields = level_json["optional_fields"]
        # Loop through optional fields
        for field_json in level_json["optional_fields"]:
            if field_json is level_json["optional_fields"]["title"]:
                level.optional_fields = cc_data.CCMapTitleField()
                level.add_field(field_json)
            if field_json is level_json["optional_fields"]["hint"]:
                level.optional_fields = cc_data.CCMapHintField()
                level.add_field(field_json)
            if field_json is level_json["optional_fields"]["password"]:
                level.optional_fields = cc_data.CCEncodedPasswordField()
                level.add_field(field_json)
        level_library.add_level(level)
    return level_library

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

with open("data/cc_data.json", "r") as reader:
    cc_data_json = json.load(reader)

cc_data = cc_dat_utils.write_cc_data_to_dat("data/cc_data.json")

