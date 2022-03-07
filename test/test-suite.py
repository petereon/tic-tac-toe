import pytest
from tic_tac_toe import generate_board, generate_board_repr
import numpy as np

def test_empty_board():
    """Test empty board
    """    
    assert generate_board() == np.zeros((3,3))


@pytest.mark.parametrize("board, expected", [
(np.zeros((3,3)), """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |

Board Created.
""")
])
def test_empty_board_repr(board, expected):
    """Test empty board repr
    """    
    assert generate_board_repr(board) == expected
