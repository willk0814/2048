def moveRight(current_board):
    return current_board


def moveLeft(current_board):
    print('called')
    for i in range(len(current_board)):

        # construct a new array of all the non empty pieces
        current_level_pieces = []
        for j in range(len(current_board[i])):
            if current_board[i][j] != '-':
                current_level_pieces.append(current_board[i][j])

        # combine like neighbors
        for j in range(0, len(current_level_pieces)):
            if current_level_pieces[j] == current_level_pieces[j - 1]:
                current_level_pieces[j - 1] *= 2
                current_level_pieces.pop(j)

        # add the necessary empty spaces
        for j in range(len(current_level_pieces), len(current_board[i])):
            current_level_pieces.append('-')

        print(current_level_pieces)
        current_board[i] = current_level_pieces

    return current_board


def moveUp(current_board):
    return current_board


def moveDown(current_board):
    return current_board


# rotate the board
def rotateBoard(current_board):
    return current_board
