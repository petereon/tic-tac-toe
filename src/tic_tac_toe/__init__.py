import numpy as np
import random
from typing import Union

player_mapping = {
    'X': 1,
    'O': -1,
    1: 'X',
    -1: 'O',
    ' ': 0,
    0: ' '
}

def generate_board():
    return np.zeros((3, 3))

def generate_board_repr(board: np.ndarray, endmes: Union[None, str]):
    if (board == np.zeros((3,3))).all():
        print(
"""Game Board Creation...
 | | 
-+-+-
 | | 
-+-+-
 | | 

Board Created.""")
    else:
        turn = len(np.argwhere(board != 0)) % 2

        if (turn == 1):
            startmes = "Player X:\n"
        else:
            startmes = "Player O:\n"

        # create board:
        boardmes = ""
        i = 0
        for row in board.tolist():
            i+=1
            boardmes+= "|".join([player_mapping[player] for player in row]) + '\n'
            if i!=3:
                boardmes+= '-+-+-\n'
        print(startmes + boardmes + '\n\n' + endmes if endmes != None else '')
            

def player_sign(possible: list, player:str) -> int:
    """
    Give random possible move
    """

    rand_num = random.randint(0, len(possible) - 1)
    return possible[rand_num]


def assess_game(board: np.ndarray, position: int) -> int:
    """
    Assess the game
    """
    row, col = divmod(position-1, 3)

    print(row, col)

    player = board[row][col]
    where_player = np.argwhere(board==player)


    # Vertical
    counter = 0
    for i,j in where_player.tolist():
        # Vertical
        if j == col:
            counter += 1
        if counter == 3:
            return player

    # Horizontal
    counter = 0
    for i,j in where_player.tolist():
        if i == row:
            counter += 1
        if counter == 3:
            return player     

    # Diagonal
    counter = 0
    for i,j in where_player.tolist():
        if i == j:
            counter += 1
        if counter == 3:
            return player

    if len(np.argwhere(board==0)) == 0:
        return 0

def play_game():
    """ Put together the game
    """



    board = generate_board()
    generate_board_repr(board)

    player = 1
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    number = player_sign(possible, player_mapping[player])


if __name__ == "__main__":
    play_game()