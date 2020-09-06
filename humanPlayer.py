import player

"""Child class of player,
This is a user Player It will capture the desire move of the user"""


class HumanPlayer(player.Player):
    def move(self):
        """ it will continue asking for a move until the user type
        any of the move array or quit to quit the game.
        Validating the user respond"""
        while True:
            move = input("'Rock', 'Paper', 'scissors'? "
                         "Type quit to exit:\n").lower()
            if move in self.moves or move == 'quit':
                return move
            print("Invalid Move!")

    def typeOfPlayer(self):
        return "Human Player"
