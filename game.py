import time

"""class game, where you can play the game, by rounds """


class Game:
    """constructor init players, and put scores in 0 """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.playerOneScore = 0
        self.playerTwoScore = 0

    """functinon to play one round"""
    def play_round(self):
        """ get the move of the players"""
        move1 = self.p1.move()
        move2 = self.p2.move()

        """ if user type quit return False to quit the game"""
        if move1 == 'quit':
            return False

        """ print move of each player """
        print(f"Player 1: {move1}  Player 2: {move2}")
        time.sleep(1)
        """if both move are the same, game tie
        if beats if true, player1 wins"""
        if move1 == move2:
            print(f"** TIE **")
        elif self.beats(move1, move2):
            print(f"** PLAYER ONE WINS **")
            self.playerOneScore += 1
        else:
            print(f"** PLAYER TWO WON **")
            self.playerTwoScore += 1

        """print the scores"""
        print(f"Score: Player One: {self.playerOneScore}\t "
              f"Player Two: {self.playerTwoScore}\n")
        """record the every move. It works on reflectPlayer and cyclePlayer"""
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        time.sleep(2)
        """User want to continue playing the game return True"""
        return True

    """start playing the game"""
    def play_game(self):
        # gameRound = 1

        print("Game start!")
        print(f"** Player 1: {self.p1.typeOfPlayer()}\t"
              f"VS\tPlayer 2: {self.p2.typeOfPlayer()} **")
        """for loop in case we want to setup a max number of games.
        we have to remove the while loop
        optional while loop continue playing until the user type quit
        while True:
            print(f"Round {gameRound}")
            if player type quit play_round is false, so we quit the game"""
        for round in range(1, 6):
            print(f"Round {round}:")
            if not self.play_round():
                break
            """gameRound += 1"""

        self.quit_game()

    """ quit game, print the scores and who won the game"""
    def quit_game(self):
        print(f"Final Score:\n Player One: {self.playerOneScore}\t"
              f" Player Two: {self.playerTwoScore}")
        """ high score won the game or some score tie game"""
        if self.playerOneScore > self.playerTwoScore:
            print("** PLAYER ONE WON THE GAME **")
        elif self.playerOneScore < self.playerTwoScore:
            print("** PLAYER TWO WON THE GAME **")
        else:
            print("** TIE GAME **")
        print("Game over!")

    """ return if player one beats player two,
    checking all the posible winning alternative"""
    def beats(self, one, two):
        return (
                (one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')
               )
