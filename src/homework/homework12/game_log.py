#write import statement for ScoreEntry
from score_entry import ScoreEntry

#create a class named GameLog with a parameterless constructor-create an empty list of score_entries class attribute in
# constructor
#Create a class method add_score_entry with a score_entry parameter, in the method code append the score_entry parameter
#to the score_entries class attribute
#Create a display_log method with no parameters-in this method iterate through display_log (score_entries???) and display each
#score entry to screen
class GameLog:
    def __init__(self):
        self.score_entries = []

    def add_score_entry(self, score_entry):
        self.score_entries.append(score_entry)

    def display_log(self):
        print("")
        for i in self.score_entries:
            print(i)
