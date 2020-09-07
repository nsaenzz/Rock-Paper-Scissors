import player

"""Child class of player, class that remembers what move it played last round,
and cycles through the different moves.
(If it played 'rock' this round, it should play 'paper' in the next round.)
If it is the first round it will return a random move"""


class OppositePlayer(player.Player):
    def move(self):
        if self.their_move == "":
            return super().randomChoice()
        elif self.their_move == "rock":
            return 'paper'
        elif self.their_move == "paper":
            return 'scissors'
        else:
            return 'rock'

    def typeOfPlayer(self):
        return "Opposite Player"
