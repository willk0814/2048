import random
import keyboard


class GameBoard:
    # method to create a blank GameBoard
    def __init__(self):
        self.board = [['-' for i in range(4)] for j in range(4)]
        self.score = 0

    # print method for the GameBoard
    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    # method to add a piece to
    def add_piece(self):
        # create a list of available indices
        available_spaces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '-':
                    available_spaces.append((i, j))
        # randomly decide where to add the piece
        row, col = available_spaces[random.randint(0, len(available_spaces) - 1)]
        # randomly decide which piece to add
        self.board[row][col] = [2] if random.randint(0, 1) == 0 else [4]

    # method to check won
    def check_won(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == [2048]:
                    return True
        return False

    # method to handle left move
    def handle_left(self):
        tmp_board = self.board

        self.board = tmp_board

    # method to handle right move
    def handle_right(self):
        tmp_board = self.board

        self.board = tmp_board

    # method to handle up move
    def handle_up(self):
        tmp_board = self.board

        self.board = tmp_board

    # method to handle down move
    def handle_down(self):
        tmp_board = self.board

        self.board = tmp_board