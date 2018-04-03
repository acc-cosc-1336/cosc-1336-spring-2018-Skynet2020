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
        
        while self.__die1 != self.__die2:
            self.__die1 = random.randint(1, 6)
            self.__die2 = random.randint(1, 6)
            print('Dice roll result:', self.__die1, self.__die2)
            if self.__die1 == self.__die2:
                print('You got the double!')
       
    def get_sideup(self):
        return self.__die1, self.__die2


