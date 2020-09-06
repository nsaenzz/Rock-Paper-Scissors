import player

""" child class of Player,
When you call the move method on a RandomPlayer object,
it should return one of 'rock', 'paper', or 'scissors' at random"""


class RandomPlayer(player.Player):
    def move(self):
        return super().randomChoice()

    def typeOfPlayer(self):
        return "Random Player"
