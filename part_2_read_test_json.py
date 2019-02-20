import json
import test_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library

    for game_data in json_data["games"]:
        game = test_data.Game()
        game.platform = test_data.Platform()
        game.title = game_data["title"]
        game.year = game_data["year"]
        game.platform.launch_year = game_data["platform"]["launch year"]
        game.platform.name = game_data["platform"]["name"]
        game_library.add_game(game)
    return game_library

    ### End Add Code Here ###

#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()

with open(input_json_file, "r") as reader:
    test_data_json = json.load(reader)

print("JSON data:")
print(test_data_json)

test_data = make_game_library_from_json(test_data_json)
print()
print("Test data:")
print(test_data)

### End Add Code Here ###
