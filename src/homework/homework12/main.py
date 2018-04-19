from player import Player
from game_log import GameLog
from die6 import Die6
from die8 import Die8
'''# write import statement for GameLog class
   # write import statements for Die6 and Die8 classes

# Create a game log instance
# ASSIGNMENT 12: Write statements to create Die6 and Die8 instances
game_log = GameLog()
die6 = Die6()
die61 = Die6()

#ASSIGNMENT12: pass the Die6 and Die8 instance object variables to the Player instantiation below as parameters after
#the game_log parameter
Player(game_log, die6, die61).roll_doubles()
game_log.display_log()


#ASSIGNMENT12: Create another GameLog instance
game_log1 = GameLog()

#ASSIGNMENT12: Write statements to create Die6 and Die8 instances
die8 = Die8()
die81 = Die8()

#ASSIGNMENT12: Create a new instance of the Player class and pass it the game log, die6, and die8 instances.
#ASSIGNMENT12: Call the player instance roll_doubles.
Player(game_log, die8, die81).roll_doubles()

#ASSIGNMENT12: Call the game log instance display_log method.
game_log.display_log()
