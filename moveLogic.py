def moveRight(current_board):
    return current_board


# -- Move Functions --
# Params:
#   current_board -> the game board before the move was made
#   current_score -> the game score before the move was made
# Returns:
#   current_board -> the resulting game board
#   current_score -> the resulting game score
def moveLeft(current_board):
    # iterate over each row
    for i in range(len(current_board)):
        # construct a new array of all the non-empty pieces
        current_level_pieces = []
        for j in range(len(current_board[i])):
            if current_board[i][j] != '-':
                current_level_pieces.append(current_board[i][j])
        # combine like neighbors
        for j in range(1, len(current_level_pieces)):
            if current_level_pieces[j] == current_level_pieces[j - 1]:
                current_level_pieces[j - 1] *= 2
                current_level_pieces.pop(j)
        # add the necessary empty spaces
        for j in range(len(current_level_pieces), len(current_board[i])):
            current_level_pieces.append('-')
        current_board[i] = current_level_pieces
    return current_board


def moveUp(current_board):
    return current_board


def moveDown(current_board):
    return current_board


# rotate the board
def rotateBoard(current_board):
    return current_board
