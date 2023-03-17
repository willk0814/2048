from GameBoard import GameBoard


def game_loop():
    # create a new GameBoard
    board = GameBoard()

    # print out the instructions
    print('\nUse the w, a, s, and d keys followed by the enter key to make moves on the board \n')

    while True:
        # add piece to the current GameBoard and print it
        board.add_piece()
        print('Current GameBoard:')
        board.print_justified_board()

        # check if the user won
        if board.check_won():
            print('\n')
            print('CONGRATULATIONS you got the 2048 tile')
            break

        # check if the user lost - no available moves and no available spaces
        if board.check_available_moves() == [] and board.find_open_spaces() == []:
            print('\n')
            print('YOU LOST')
            break

        # prompt the user for an input {w, a, s, d}
        valid_move_made, valid_moves = False, board.check_available_moves()
        while not valid_move_made:
            user_move = input('Make your move using the w, a, s, and d keys \n').strip().replace(" ", '')
            if user_move in valid_moves:
                board.handleMove(user_move)
                valid_move_made = True
            else:
                print('Looks like that move is unavailable \n')
                board.print_justified_board()


if __name__ == '__main__':
    game_loop()

