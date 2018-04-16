#write import statements for Player and Die class
from die import Die
from player import Player

#Create an instance of the Main class and call/execute the roll_doubles method
def main():
    dice = Player()
    
    print('Rolling the dice')
    dice.roll_doubles()

main()
