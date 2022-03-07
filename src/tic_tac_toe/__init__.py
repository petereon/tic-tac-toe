import numpy as np
import random

def generate_board():
    return np.zeros((3, 3))

def generate_board_repr(board: np.ndarray):
    print(
"""Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |

Board Created.""")

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


if __name__ == "__main__":
    board = generate_board()
    generate_board_repr(board)

    player = 1
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    player_sign(possible, player)