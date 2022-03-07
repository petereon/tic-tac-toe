import pytest
import numpy as np
from tic_tac_toe import(
    generate_board, 
    generate_board_repr, 
    player_sign, 
    assess_game, 
    play_game) 


def test_empty_board():
    """Test empty board
    """    
    assert (generate_board() == np.zeros((3,3))).all()


@pytest.mark.parametrize("board,endmes,expected", [
(np.zeros((3,3)), None, """Game Board Creation...
 | | 
-+-+-
 | | 
-+-+-
 | | 

Board Created."""),
(np.array([[1,0,0],[1,-1,0],[1,0,-1]]),"PLAYER X WON!", """Player X:
X| | 
-+-+-
X|O| 
-+-+-
X| |O

PLAYER X WON!"""),
(np.array([[1,0,1],[-1,-1,-1],[1,0,0]]),"PLAYER O WON!","""Player O:
X| |X
-+-+-
O|O|O
-+-+-
X| | 

PLAYER O WON!"""),
(np.array([[1,0,0],[-1,1,0],[-1,0,1]]),"PLAYER X WON!", """Player X:
X| | 
-+-+-
O|X| 
-+-+-
O| |X

PLAYER X WON!"""),
(np.array([[1,-1,1],[-1,-1,1],[1,1,-1]]),"GAME ENDS WITH A DRAW!","""Player X:
X|O|X
-+-+-
O|O|X
-+-+-
X|X|O

GAME ENDS WITH A DRAW!""")
])
def test_board_repr(board, endmes, expected, capsys):
    """Test empty board repr
    """
    generate_board_repr(board, endmes)
    captured, err = capsys.readouterr()    
    assert captured.replace('\n', '') == expected.replace('\n', '')

@pytest.mark.parametrize("possible,player,expected_range", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 'X', [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([2, 4, 5], 'O', [2, 4, 5]),
    ([9], 'X', [9])
]

)
def test_player_sign(possible, player, expected_range):
    """Test where a player puts his sign
    """
    res = player_sign(possible, player)
    assert res in expected_range

@pytest.mark.parametrize("board,position,expected", [
    (np.array([[1,0,0],[-1,1,0],[-1,0,1]]), 9, 1),
    (np.array([[1,0,0],[1,-1,0],[1,-1,0]]), 1, 1),
    (np.array([[1,0,1],[-1,-1,-1],[1,0,0]]), 6, -1),
    (np.array([[1,-1,1],[-1,-1,1],[1,1,-1]]), 7, 0),
    (np.array([[1,0,-1],[0,0,0],[0,0,0]]), 3, None)
])
def test_asses_game(board, position, expected):
    """Test asses game
    """
    assert assess_game(board, position) == expected


def test_play_game(capsys):
    play_game()
    captured, err = capsys.readouterr() 

#     assert """Game Board Creation...
#  | |
# -+-+-
#  | |
# -+-+-
#  | |

# Board Created.""".replace('\n', '') in captured.replace('\n', '')

    assert ("PLAYER X WON!" in captured)  or ("PLAYER O WON!" in captured) or ("GAME IS DRAW!" in captured)