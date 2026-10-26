import pytest

from main import parse_move, render_board, play_game
from board import Board, MARK_O, MARK_X
from game import Game

X_WIN_INPUTS = ["1 1", "2 1", "1 2", "2 2", "1 3"]
DRAW_INPUTS = ["1 1", "1 2", "1 3", "2 2", "2 1", "3 1", "2 3", "3 3", "3 2"]

def run(inputs):
    """Play one game with scripted inputs.
    
    Return the game and what was shown."""
    lines = iter(inputs)
    shown = []
    game = Game()
    play_game(game, read=lambda prompt: next(lines), write=shown.append)
    return game, shown

@pytest.mark.parametrize("text, expected", [
    ("1 1", (0, 0)),
    ("3 3", (2, 2)),
    ("2 3", (1, 2)),
    ("  2  3  ", (1, 2)),
])
def test_valid_move_is_converted_to_zero_based(text, expected):
    assert parse_move(text, 3) == expected

@pytest.mark.parametrize("text", ["a b", "one 2", "1", "1 2 3", "0.5 1", "", " ",])
def test_non_numeric_or_wrong_count_input_shows_a_clear_message(text):
    with pytest.raises(ValueError, match="two numbers"):
        parse_move(text, 3)

@pytest.mark.parametrize("text", ["0 1", "1 0", "-1 1", "1 -1", "4 1", "1 4"])
def test_out_of_range_input_shows_a_clear_message(text):
    with pytest.raises(ValueError, match="between 1 and 3"):
        parse_move(text, 3)

def test_render_board_shows_every_cell_with_numbers_for_rows_and_columns():
    board = Board()

    assert board.place_mark(0, 0, MARK_X)
    assert board.place_mark(0, 1, MARK_O)
    assert board.place_mark(1, 1, MARK_X)

    assert render_board(board) == "\n".join([
        " X | O |",
        "---+---+---",
        "   | X |",
        "---+---+---",
        "   |   |"
    ])

def test_x_wins_and_the_winner_is_annouces():
    game, shown = run(X_WIN_INPUTS)

    assert game.winner == MARK_X
    assert shown[-1] == "X wins!"