class ScoreEntry:

    def __init__(self, score_entry_id, die1_value, die2_value):
        self.score_entry_id = score_entry_id
        self.die1_value = die1_value
        self.die2_value = die2_value
        #create public class attributes for each parameter

    def __str__(self):
        return str(self.score_entry_id) + " " + str(self.die1_value) + " " + str(self.die2_value)
