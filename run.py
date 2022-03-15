import random


def print_board(board):
    """
    This function prints the board out, which consists of a list of
    10 strings representing the cells in the board (ignore index 0)
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
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
        letter = input().upper()

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


def is_winner(bo, le):
    """
    Returns True if a player has won. bo is used for board
    and le for letter to shorten the code.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down left
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down right
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


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
                print('Well done! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    print_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
                    