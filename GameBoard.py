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

    # method to add a piece to the board
    def add_piece(self):
        # create a list of available indices
        available_spaces = self.find_open_spaces()
        # randomly decide where to add the piece
        row, col = available_spaces[random.randint(0, len(available_spaces) - 1)]
        # randomly decide which piece to add
        self.board[row][col] = [2] if random.randint(0, 1) == 0 else [4]

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
        available_moves = []
        current_board = self.board

        # check each move to see if it yields the same board
        if current_board == moveLogic.moveUp(current_board):
            available_moves.append('w')
        if current_board == moveLogic.moveDown(current_board):
            available_moves.append('s')
        if current_board == moveLogic.moveLeft(current_board):
            available_moves.append('a')
        if current_board == moveLogic.moveRight(current_board):
            available_moves.append('d')

        return available_moves

    # call the correct move function based on the users input
    def handleMove(self, player_move):
        current_board = self.board

        if player_move == 'W' or player_move == 'w':
            current_board = moveLogic.moveUp(current_board)
        elif player_move == 'A' or player_move == 'a':
            current_board = moveLogic.moveRight(current_board)
        elif player_move == 'S' or player_move == 's':
            current_board = moveLogic.moveDown(current_board)
        elif player_move == 'D' or player_move == 'd':
            current_board = moveLogic.moveRight(current_board)

        self.board = current_board

        return current_board
