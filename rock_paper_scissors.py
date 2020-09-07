import game
import random
import time
import humanPlayer
import randomPlayer
import cyclePlayer
import reflectPlayer
import rockPlayer
import oppositePlayer

"""This program plays a game of Rock, Paper,
Scissors between two selected Players (User or computer),
and reports both Player's scores each round."""


def selectPlater():
    while True:
        print("1 - Human Player (user player)")
        print("2 - Random Player (plays random between rock, paper, scissors)")
        print("3 - Oppsite Player (plays last round oppsite move)")
        print("4 - Reflect Playe (plays opponent last move")
        print("5 - Cycle Player (always plays rock)")
        print("6 - Rock Player (always plays rock)")
        print("7 - Please select for me (Computer select a non human "
              "Player from the list above)")
        player = input("Please select a player. Type 1, 2, 3, 4, 5, "
                       "6, or 7: \n")
        if player == "7":
            player = random.choice(["2", "3", "4", "5", "6"])

        if player == "1":
            return humanPlayer.HumanPlayer()
        elif player == "2":
            return randomPlayer.RandomPlayer()
        elif player == "3":
            return oppositePlayer.OppositePlayer()
        elif player == "4":
            return reflectPlayer.ReflectPlayer()
        elif player == "5":
            return cyclePlayer.CyclePlayer()
        elif player == "6":
            return rockPlayer.RockPlayer()


def intro():
    print("*** Welcome to Rock, Paper, Scissors' game**")
    print("This game has five rounds,")


def main():
    intro()
    time.sleep(1)

    print("Players 1:")
    player1 = selectPlater()
    print(f"{player1.typeOfPlayer()} selected")
    time.sleep(1)

    print("Players 2:")
    player2 = selectPlater()
    print(f"{player2.typeOfPlayer()} selected")
    time.sleep(1)

    gameRPC = game.Game(player1, player2)
    # game = Game(humanPlayer.HumanPlayer(), randomPlayer.RandomPlayer())
    # game = Game(humanPlayer.HumanPlayer(), cyclePlayer.CyclePlayer())
    # game = Game(humanPlayer.HumanPlayer(), reflectPlayer.ReflectPlayer())
    # game = Game(humanPlayer.HumanPlayer(), rockPlayer.RockPlayer())
    gameRPC.play_game()


if __name__ == '__main__':
    main()
