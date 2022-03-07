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

def player_sign(possible: np.ndarray, player:str) -> int:
    pass