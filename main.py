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
        board.print_board()

        # check if the user won
        if board.check_won():
            print('CONGRATULATIONS you got the 2048 tile')
            break

        # check if the user lost - no available moves and no available spaces
        # if board.check_available_moves() == [] and board.find_open_spaces() == []:
        #     print('YOU LOST')
        #     break

        # prompt the user for an input {w, a, s, d}
        user_move = input('Make your move using the w, a, s, and d keys \n').strip()
        print(user_move)
        board.handleMove(user_move)


if __name__ == '__main__':
    game_loop()
