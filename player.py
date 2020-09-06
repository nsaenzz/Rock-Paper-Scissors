import random

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """constructor clase, initial values of my_move,
    opponent move, and all availables moves"""
    def __init__(self):
        self.my_move = ""
        self.their_move = ""
        self.moves = ['rock', 'paper', 'scissors']

    """declare funnction move, Every player have different move"""
    def move(self):
        pass

    """ save the moves the playar and opponent"""
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    """ return a random move from the move array"""
    def randomChoice(self):
        return random.choice(self.moves)

    def typeOfPlayer(self):
        pass
