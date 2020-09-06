import player

""" child class of Player,
This player always play rock"""


class RockPlayer(player.Player):
    def move(self):
        return "rock"

    def typeOfPlayer(self):
        return "Rock Player"
