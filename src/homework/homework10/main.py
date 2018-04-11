from player import Player
from game_log import GameLog

# write import statement for GameLog class


# Create a game log instance
output = GameLog()

# SEnd the game_log instance to Player class as an argument
Player(output).roll_doubles()

# call the game log display method below
output.display_log()
