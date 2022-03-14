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
        # First character is player's letter, and second the computers
        return ['X', 'O']  
    else:
        return ['O', 'X']