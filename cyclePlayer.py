import player

"""Child class of player, class that remembers what move it played last round,
and cycles through the different moves.
(If it played 'rock' this round, it should play 'paper' in the next round.)
If it is the first round it will return a random move"""


class CyclePlayer(player.Player):
    def move(self):
        if self.my_move == "":
            return super().randomChoice()
        elif self.my_move == "rock":
            return 'paper'
        elif self.my_move == "paper":
            return 'scissors'
        else:
            return 'rock'

    def typeOfPlayer(self):
        return "Cycle Player"
