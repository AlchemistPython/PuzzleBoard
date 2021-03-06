from puzzleboard import Puzzle
from player import Player

class Game(Puzzle):
    
    def __init__(self):
        super().__init__()
        self.__counter = 100
    
    @staticmethod
    def instructions():
        """Static Method that I use to show instructions to the puzzle game."""
        print("""Welcome to Puzzle Game 
              Instructions:
              
              1.- Order the numbers equal at level showed.
              
              2.- Every change of numbers will rest the points given at the beginning.
              
              3.- If the points are equal to 0, the game it's over. 
              
              From the next puzzles select one of them to solve.
              
              1.- Horizontal.
              2.- Vertical
              3.- Diagonal
              4.- Snail
              5.- Spiral
              6.- Impossible
              """)
    @property
    def score(self):
        return self.__counter
    
    def points(self):
        self.__counter -= 1
        return self.__counter             

def start_game():
    Game().instructions()
    type_board = input("Select the number of board: ")
    player_name = input("Your Player Name is: ")
    # instance three objects
    new_game = Game()
    new_game.kind = type_board
    new_game.whatBoard()
    print("Puzzle to solve")
    new_game.fillBoard()
    print(new_game.score)
    # begin the puzzle
    while True:
        number = input("What number move? ")
        new_game.number = number
        new_game.swapItems(new_game.number)
        new_game.points()
        print(f"Score: {new_game.score}")
        if new_game.compareBoard():
            print("End Game, you win!")
            break
        elif new_game.score == 0:
            print("End Game, you lost. Your points are up.")
            break
        
start_game()