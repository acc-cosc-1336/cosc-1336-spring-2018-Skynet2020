from die import Die
import random
#write import statement for Die class

'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.__die1 = Die()
        self.__die2 = Die()
        

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        rolled_double = False
        while rolled_double == False:
            roll1 = self.__die1.roll()
            roll2 = self.__die2.roll()
            print('Dice roll result:', roll1, roll2)
            rolled_double = roll1 == roll2
