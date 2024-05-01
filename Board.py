from typing import List
from utils import Shape, DEFAULT_STARTING_SHAPE


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.winner = None

    def end_condition(self):
        return self.board_full() or self.winner != None

    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.board[i][0]
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.board[0][i]
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
            return

    def get_board(self):
        return self.board

    def get_winner(self):
        return self.winner

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def enter_move(self, coordinates_input: List[int], shape_turn: Shape):
        self.board[coordinates_input[0]-1][coordinates_input[1]-1] = shape_turn

    def do_turn(self, shape_turn: Shape):
        coordinates_input = input(f"It's {shape_turn}'s turn. Please make your move by entering coordinates (for example, the middle square will be: '2,2')")
        coordinates_input = [int(coord) for coord in coordinates_input.split(',')]
        self.enter_move(coordinates_input, shape_turn)

