from enum import Enum
import sys
import Board

class Shape(Enum):
    O = "O"
    X = "X"

DEFAULT_STARTING_SHAPE = Shape.X

def main(starting_shape: Shape):
    shape_turn = starting_shape
    board = Board.Board()
    board.print_board()

    while not board.end_condition():
        board.do_turn(shape_turn)
        board.print_board()

        shape_turn = Shape.O if shape_turn == Shape.X else Shape.X


    if board.winner == Shape.X:
        print("winner is X")
    elif board.winner == Shape.O:
        print("winner is O")
    else:
        print("There is a tie")


if __name__ == "__main__":
    starting_shape = DEFAULT_STARTING_SHAPE
    if len(sys.argv) > 1:
        starting_shape = sys.argv[1]
    main(starting_shape)
