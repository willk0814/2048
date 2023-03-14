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
            print('Congratulations you got the 2048 tile')
            break

        # prompt the user for an input {w, a, s, d}
        user_move = input('\nMake your move using the arrow keys \n')

        # handle user move and update GameBoard and score
        if user_move == 'W' or user_move == 'w':
            board.handle_up()
        elif user_move == 'A' or user_move == 'a':
            board.handle_left()
        elif user_move == 'S' or user_move == 's':
            board.handle_down()
        elif user_move == 'D' or user_move == 'd':
            board.handle_right()


if __name__ == '__main__':
    game_loop()
