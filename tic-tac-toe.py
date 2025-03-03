import math
import random 

class Player:
    def __init__(self,letter):
        #letter is x or 0
        
        self.letter = letter
    # we want player tp be able to get their next move 
    def get_move(self, game):
        pass
    
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        squre = random.choice(game.avaliable_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.input move (0-9): ' )