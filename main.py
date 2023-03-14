import random
import keyboard


class GameBoard:
    # func to create a blank GameBoard
    def __init__(self):
        self.board = [['-' for i in range(4)] for j in range(4)]
        self.score = 0

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

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

    def handle_left(self):
        tmp_board = self.board

        self.board = tmp_board

    def handle_right(self):
        tmp_board = self.board

        self.board = tmp_board

    def handle_up(self):
        tmp_board = self.board

        self.board = tmp_board

    def handle_down(self):
        tmp_board = self.board

        self.board = tmp_board


def game_loop():
    # create a new GameBoard
    board = GameBoard()

    while True():
        board.add_piece()
        board.print_board()

        # prompt the user for an input {up, down, left, right}
        print('\n' + 'Make your move using the arrow keys')

        break


if __name__ == '__main__':
    game_loop()
