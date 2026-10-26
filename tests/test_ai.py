import random
import pytest

from ai import AIPlayer, EasyAI
from board import Board, MARK_O, MARK_X

SEEDS = [0, 1, 2, 3, 7]

def rng(seed=7):
    return random.Random(seed)

def fill(board, marks_by_cell):
    """Place marks given as {(row, col): mark}."""
    for (row, col), mark in marks_by_cell.items():
        assert board.place_mark(row, col, mark)


def test_abstract_ai_cannot_be_created():
    with pytest.raises(TypeError):
        AIPlayer(rng())

def test_easy_is_an_ai_player():
    assert isinstance(EasyAI(rng()), AIPlayer)

@pytest.mark.parametrize("seed", SEEDS)
def test_easy_always_returns_an_empty_cell(seed):
    board = Board()
    fill(board, {
        (0, 0): MARK_X,
        (1, 1): MARK_O,
        (2, 2): MARK_X
    })

    move = EasyAI(rng(seed)).choose_move(board, MARK_O)

    assert move in board.empty_cells()

def test_easy_takes_the_only_empty_cell():
    board = Board()
    fill(board, {
        (0, 0): MARK_X, (0, 1): MARK_O, (0, 2): MARK_X,
        (1, 0): MARK_X, (1, 1): MARK_O, (1, 2): MARK_X,
        (2, 0): MARK_O, (2, 1): MARK_X,
    })

    assert EasyAI(rng()).choose_move(board, MARK_O) == (2, 2)

def test_easy_leaves_the_board_unchanged():
    board = Board()
    fill(board, {
        (0, 0): MARK_X,
        (1, 1): MARK_O,
        (0, 1): MARK_X
    })
    before = board.empty_cells()

    EasyAI(rng()).choose_move(board, MARK_O)

    assert board.empty_cells() == before