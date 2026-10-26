import pytest

from board import MARK_O, MARK_X
from game import Game

OFF_BOARD = [(-1, -1), (-1, 2), (0, -1), (3, 2), (0, 3), (3, 6)]

# X wins on the top row with their third move.
X_WINS_ROW = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]

# X O X
# X O X
# O X O
DRAW_MOVES = [
    (0, 0), (0, 1), (0, 2), (1, 1), (1, 0),
    (2, 0), (1, 2), (2, 2), (2, 1)
]

# X O X
# O X O
# O X X
WIN_ON_LAST_MOVE = [
    (0, 0), (0, 1), (0, 2), (1, 0), (1, 1),
    (1, 2), (2, 1), (2, 0), (2, 2)
]

@pytest.fixture
def game():
    """A fresh game."""
    return Game()

def play(game, moves):
    """Make every move in moves, which all must be accepted."""
    for row, col in moves:
        assert game.take_turn(row, col)

def test_new_game_starts_with_x(game):
    assert game.current_player == MARK_X

def test_new_game_has_no_winner_and_is_not_over(game):
    assert game.winner is None
    assert not game.is_draw
    assert not game.is_over

def test_valid_move_passes_the_turn_to_other_player(game):
    assert game.take_turn(0, 0)

    # X starts first, so 2nd move will be by O
    assert game.current_player == MARK_O

def test_players_alternate_x_o_x(game):
    play(game, [(0, 0), (0, 1)])

    assert game.current_player == MARK_X

def test_taken_cell_is_rejected_and_keeps_the_turn(game):
    play(game, [(1, 2)])    # next turn is O's

    assert not game.take_turn(1, 2)
    assert game.current_player == MARK_O

@pytest.mark.parametrize("row, col", OFF_BOARD)
def test_off_board_move_is_rejected_and_keeps_the_turn(game, row, col):
    assert not game.take_turn(row, col)

    assert game.current_player == MARK_X

def test_winning_move_is_reported(game):
    play(game, X_WINS_ROW)

    assert game.winner == MARK_X
    assert game.is_over
    assert not game.is_draw

def test_full_board_without_a_winner_is_a_draw(game):
    play(game, DRAW_MOVES)

    assert game.winner is None
    assert game.is_draw
    assert game.is_over

def test_last_move_that_fills_the_board_and_wins_is_a_win_not_a_draw(game):
    play(game, WIN_ON_LAST_MOVE)

    assert game.winner == MARK_X
    assert not game.is_draw
    assert game.is_over

def test_no_moves_are_accepted_after_the_game_is_over(game):
    play(game, X_WINS_ROW)

    assert not game.take_turn(2, 2)

def test_board_reflects_moves_made_through_the_game(game):
    assert len(game.board.empty_cells())

    play(game, [(0, 0)])

    assert game.board.cell(0, 0) == MARK_X