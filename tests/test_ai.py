import random
import pytest

from ai import AIPlayer, EasyAI, HardAI
from board import Board, MARK_O, MARK_X

SEEDS = [0, 1, 2, 7]

# ------- helper functions --------

def rng(seed=7):
    return random.Random(seed)

def fill(board, marks_by_cell):
    """Place marks given as {(row, col): mark}."""
    for (row, col), mark in marks_by_cell.items():
        assert board.place_mark(row, col, mark)

def play_every_x_move(board, ai):
    """Try every x move from here, with hardAI replying as O.

    Return the number of finished games. Fail if X ever wins.
    """
    games = 0
    
    for row, col in board.empty_cells():
        assert board.place_mark(row, col, MARK_X)
        assert not board.has_won(MARK_X)

        if board.is_full():
            games += 1
        else:
            r, c = ai.choose_move(board, MARK_O)
            assert board.place_mark(r, c, MARK_O)
            if board.has_won(MARK_O):
                games += 1
            else:
                games += play_every_x_move(board, ai)
            board.remove_mark(r, c)

        board.remove_mark(row, col)

    return games

# ------- helper functions ----------

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

def test_hard_leaves_the_board_unchanged():
    board = Board()
    fill(board, {
        (0, 0): MARK_X,
        (1, 1): MARK_O,
        (0, 1): MARK_X
    })
    before = board.empty_cells()

    HardAI(rng()).choose_move(board, MARK_O)

    assert board.empty_cells() == before

@pytest.mark.parametrize("seed", SEEDS)
def test_hard_takes_a_winning_move_when_one_exists(seed):
    board = Board()

    # X X .
    # O O .
    # . . .
    fill(board, {
        (0, 0): MARK_X, (1, 0): MARK_O,
        (0, 1): MARK_X, (1, 1): MARK_O,
    })

    assert HardAI(rng(seed)).choose_move(board, MARK_O) == (1, 2)

@pytest.mark.parametrize("seed", SEEDS)
def test_hard_blocks_when_it_cannot_win(seed):
    board = Board()

    # X X .
    # . O .
    # . . .
    fill(board, {
        (0, 0): MARK_X, (1, 1): MARK_O,
        (0, 1): MARK_X
    })

    assert HardAI(rng(seed)).choose_move(board, MARK_O) == (0, 2)

def test_hard_never_loses_when_it_plays_second():
    games = play_every_x_move(Board(), HardAI(rng()))

    assert games > 0