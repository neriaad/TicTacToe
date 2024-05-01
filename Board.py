class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def end_condition(self):
        return self.board_full(self.board) or self.winner != None

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

    def do_turn(self, shape_turn):
        pass
