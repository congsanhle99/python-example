import random
import sys


class RPS:
    def __init__(self):
        print("""
            Enter rock or paper or scissors to play game.
            Enter 'exit' if you don't wanna play it.
            """)
        self.moves: dict = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("rock or paper or scissors>> ").lower()
        if user_move == "exit":
            print("Bye!!!")
        if user_move not in self.valid_moves:
            print("Invalid move!!!")
            return self.play_game()

        computer_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, computer_move)
        self.check_move(user_move, computer_move)

    def display_moves(self, user_move: str, computer_move: str):
        print("------------------")
        print(f'You: {self.moves[user_move]}')
        print(f'Computer: {self.moves[computer_move]}')
        print("------------------")

    def check_move(self, user_move: str, computer_move: str):
        if user_move == computer_move:
            print("TIE!!!")
        elif user_move == "rock" and computer_move == "scissors":
            print("YOU WIN!!!")
        elif user_move == "scissors" and computer_move == "paper":
            print("YOU WIN!!!")
        elif user_move == "paper" and computer_move == "rock":
            print("YOU WIN!!!")
        else:
            print("COMPUTER WIN!!!")


if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()
