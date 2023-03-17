import copy
import random
import moveLogic


class GameBoard:
    # method to create a blank GameBoard
    def __init__(self):
        self.board = [['-' for i in range(4)] for j in range(4)]
        self.score = 0

    # print method for the GameBoard
    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    # print a justified version of the board
    def print_justified_board(self):
        justified_board = []
        # establish the largest valued piece on the board
        _max = 0
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[i])):
                row.append(self.board[i][j])
                _max = len(str(self.board[i][j])) if len(str(self.board[i][j])) > _max else _max
            justified_board.append(row)

        # add the appropriate padding to each cell
        for i in range(len(justified_board)):
            for j in range(len(justified_board[i])):
                # reassign '-' to '_'
                if justified_board[i][j] == '-':
                    justified_board[i][j] = '_' * _max
                else:
                    justified_board[i][j] = '_' * (_max - len(str(justified_board[i][j]))) \
                                            + str(justified_board[i][j])

        for i in range(len(justified_board)):
            print(justified_board[i])

    # method to add a piece to the board
    def add_piece(self):
        # create a list of available indices
        available_spaces = self.find_open_spaces()
        # randomly decide where to add the piece
        row, col = available_spaces[random.randint(0, len(available_spaces) - 1)]
        # randomly decide which piece to add
        self.board[row][col] = 2 if random.randint(0, 1) == 0 else 4

    # method that returns a list of available coordinate pairs
    def find_open_spaces(self):
        available_spaces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '-':
                    available_spaces.append((i, j))
        return available_spaces

    # method to check won
    def check_won(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == [2048]:
                    return True
        return False

    # method to check if there are any available moves
    def check_available_moves(self):
        available_moves, current_board = [], []
        # create temporary board
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[i])):
                row.append(self.board[i][j])
            current_board.append(row)

        tmp_board = copy.deepcopy(current_board)
        # check each move to see if it yields the same board
        if current_board != moveLogic.moveUp(tmp_board):
            available_moves.append('w')
        if current_board != moveLogic.moveDown(tmp_board):
            available_moves.append('s')
        if current_board != moveLogic.moveLeft(tmp_board):
            available_moves.append('a')
        if current_board != moveLogic.moveRight(tmp_board):
            available_moves.append('d')

        return available_moves

    # call the correct move function based on the users input
    def handleMove(self, player_move):

        if player_move == 'W' or player_move == 'w':
            self.board = moveLogic.moveUp(self.board)
        elif player_move == 'A' or player_move == 'a':
            self.board = moveLogic.moveLeft(self.board)
        elif player_move == 'S' or player_move == 's':
            self.board = moveLogic.moveDown(self.board)
        elif player_move == 'D' or player_move == 'd':
            self.board = moveLogic.moveRight(self.board)
