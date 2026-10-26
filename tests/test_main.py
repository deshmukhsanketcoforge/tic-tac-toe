import pytest

from main import parse_move, render_board, play_game, NOT_NUMBERS
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

def test_full_board_without_a_winner_is_announced_as_a_draw():
    game, shown = run(DRAW_INPUTS)

    assert game.is_draw
    assert shown[-1] == "It's a draw."

def test_board_is_shown_at_the_start_and_after_every_move():
    _, shown = run(X_WIN_INPUTS)

    boards = [text for text in shown if text.startswith(" ")]
    assert len(boards) == len(X_WIN_INPUTS)

def test_non_numeric_input_shows_a_message_and_keeps_the_turn():
    game, shown = run(["a b"] + X_WIN_INPUTS)

    assert NOT_NUMBERS in shown
    assert game.winner == MARK_X        # X still got the first move

def test_taken_cell_shows_a_message_and_keeps_the_turn():
    game, shown = run(["1 1", "1 1", "2 1", " 1 2", "2 2", "1 3"])

    assert "That cell is already taken." in shown
    assert game.winner == MARK_X    # duplicate (1, 1) move not considered valid and turn kept