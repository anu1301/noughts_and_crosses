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


def input_letter_choice():
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


def reset_board(board):
    # Resets board
    reset_board = []

    for i in board:
        reset_board.append(i)

    return reset_board


def is_space_free(board, move):
    # Checks if a move is available
    return board[move] == ' '


def get_player_move(board):
    # Allows the player to make his/her move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Make your next move(1-9)')
        move = input()
    return int(move)         
