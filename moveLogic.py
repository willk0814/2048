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
        for j in range(len(current_level_pieces) - 1):
            if current_level_pieces[j] == current_level_pieces[j + 1]:
                current_level_pieces[j] *= 2
                current_level_pieces[j + 1] = '-'
        # remove any blank spaces
        current_level_pieces = [i for i in current_level_pieces if i != '-']
        # add the necessary empty spaces
        current_level_pieces += '-' * (len(current_board) - len(current_level_pieces))
        # assign the new row
        current_board[i] = current_level_pieces
    return current_board


def moveRight(current_board):
    return rotateBoardRight(rotateBoardRight(moveLeft(rotateBoardLeft(rotateBoardLeft(current_board)))))


def moveUp(current_board):
    return rotateBoardRight(moveLeft(rotateBoardLeft(current_board)))


def moveDown(current_board):
    return rotateBoardLeft(moveLeft(rotateBoardRight(current_board)))


def rotateBoardLeft(current_board):
    return transposeMatrix(reverseMatrix(current_board))


def rotateBoardRight(current_board):
    return reverseMatrix(transposeMatrix(current_board))


def reverseMatrix(current_board):
    for i in range(len(current_board)):
        current_board[i].reverse()
    return current_board


def transposeMatrix(current_board):
    for i in range(len(current_board)):
        for j in range(i, len(current_board)):
            current_board[i][j], current_board[j][i] = current_board[j][i], current_board[i][j]
    return current_board

