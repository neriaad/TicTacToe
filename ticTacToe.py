import sys
import Board
from utils import Shape, DEFAULT_STARTING_SHAPE


def main(starting_shape: Shape):
    shape_turn = starting_shape
    board = Board.Board()
    board.print_board()

    while not board.end_condition():
        board.do_turn(shape_turn)
        board.print_board()
        board.check_winner()

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
