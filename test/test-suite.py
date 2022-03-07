import pytest
from tic_tac_toe import generate_board, generate_board_repr, player_sign
import numpy as np

def test_empty_board():
    """Test empty board
    """    
    assert (generate_board() == np.zeros((3,3))).all()


@pytest.mark.parametrize("board, expected", [
(np.zeros((3,3)), """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |

Board Created.""")
])
def test_empty_board_repr(board, expected, capsys):
    """Test empty board repr
    """
    generate_board_repr(board)
    captured, err = capsys.readouterr()    
    assert captured.replace('\n', '') == expected.replace('\n', '')

@pytest.mark.parametrize("possible,player,expected_range", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 'X', [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([2, 4, 5], 'O', [2, 3, 5]),
    ([9], 'X', [9])
]

)
def test_player_sign(possible, player, expected_range):
    """Test where a player puts his sign
    """
    res = player_sign(possible, player)
    assert res in expected_range
