import player

""" child class of Player, lass that remembers
what move the opponent played last round,
and plays that move this round.
(In other words, if user plays 'paper' on the first round,
a ReflectPlayer will play 'paper' on the second round.)
If it is the first round it will return a random move"""


class ReflectPlayer(player.Player):
    def move(self):
        return self.their_move if self.their_move else super().randomChoice()

    def typeOfPlayer(self):
        return "Reflect Player"
