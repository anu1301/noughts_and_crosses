import random

print("\033[1;36m")
print("NOUGHTS & CROSSES".center(30, "="))
print("\n")


def print_board(board):
    """
    This function prints the board out, which consists of a list of
    10 strings representing the cells in the board (ignore index 0)
    """
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def input_player_letter():
    """
    Lets the player choose X or O.
    Returns as list with the player's choice as first item,
    and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper().isalpha()

        try:
            letter.isalpha()
        except:
            print("Please enter X or O")

    if letter == 'X':
        # First character is player's letter,
        # and second the computers
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_starts_play():
    """
    Randomly choose the player who plays first.
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    """
    Returns True if the player wants to play agian.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def making_move(board, letter, move):
    board[move] = letter


def is_winner(brd, lttr):
    """
    Returns True if a player has won. brd is used for board
    and lttr for letter to shorten the code.
    """
    return (
        (brd[1] == lttr and brd[2] == lttr and brd[3] == lttr) or  # top line
        (brd[4] == lttr and brd[5] == lttr and brd[6] == lttr) or  # mid line
        (brd[7] == lttr and brd[8] == lttr and brd[9] == lttr) or  # bottom
        (brd[1] == lttr and brd[4] == lttr and brd[7] == lttr) or  # down left
        (brd[2] == lttr and brd[5] == lttr and brd[8] == lttr) or  # mid line
        (brd[3] == lttr and brd[6] == lttr and brd[9] == lttr) or  # down right
        (brd[3] == lttr and brd[5] == lttr and brd[7] == lttr) or  # diagonal
        (brd[1] == lttr and brd[5] == lttr and brd[9] == lttr)  # diagonal
    )


def get_board_copy(board):
    """
    Creates a copy board
    """
    copy_board = []

    for i in board:
        copy_board.append(i)

    return copy_board


def is_space_free(board, move):
    """
    Checks if a move is available
    """
    return board[move] == ' '


def get_player_move(board):
    """
    Allows the player to make his/her move
    """
    move = ' '
    while (
        move not in '1 2 3 4 5 6 7 8 9'.split() or
        not is_space_free(board, int(move))
    ):
        print('Make your next move(1-9)')
        move = input()
    return int(move)


def choose_random_move(board, moves_list):
    """
    Returns a valid move and returns None if there is no valid move.
    """
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    """
    Computer determines where to move and returns that move.
    """
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Checks if the player can win in next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            making_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Checks if corners are free and makes move.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Checkes if center is free and makes move
    if is_space_free(board, 5):
        return 5

    # Checks sides and make move.
    return choose_random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    """
    Checks to see if every space on the board has been taken,
    and returns True, Otherwise returns False.
    """
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Noughts & Crosses!')

while True:
    """
    Resets the board
    """
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_starts_play()
    print('The ' + turn + ' will go first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn.
            print_board(the_board)
            move = get_player_move(the_board)
            making_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                print_board(the_board)
                print('Well done! You won this game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    print_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = get_computer_move(the_board, computer_letter)
            making_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                print_board(the_board)
                print('The computer won this game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    print_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        print("Thank you for playing")
        break
