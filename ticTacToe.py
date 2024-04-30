from enum import Enum
import Board

class Shape(Enum):
    O = "O"
    X = "X"

def main(starting_shape: Shape):
    shape_turn = starting_shape
    board = Board.Board()

    while not board.end_condition():
        board.do_turn(shape_turn)
        board.print_board()

        shape_turn = Shape.O if shape_turn == Shape.X else Shape.X


    if board.winner == Shape.X:
        print("winner is x")
    elif board.winner == Shape.O:
        print("winner is O")
    else:
        print("There is a tie")




if __name__ == "__main__":
    main()
