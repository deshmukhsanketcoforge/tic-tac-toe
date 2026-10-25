import pytest

from board import Board
from board import EMPTY, MARK_O, MARK_X

OFF_BOARD = [(-1, -1), (-1, 2), (0, -1), (3, 2), (0, 3), (3, 6)]

@pytest.fixture
def board():
    """A fresh, empty 3x3 board for each test."""
    return Board()

def test_board_size_returns_actual_size(board):
    assert board.size == 3

@pytest.mark.parametrize("size", [2, 1, 0, -1])
def test_board_smaller_than_3_is_rejected(size):
    with pytest.raises(ValueError, match="size must be at least 3"):
        Board(size)

@pytest.mark.parametrize("size", [3, 4, 5])
def test_board_3_or_larger_is_accepted(size):
    assert Board(size).size == size

def test_new_board_lists_all_nine_cells_as_empty(board):
    assert board.empty_cells() == [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

@pytest.mark.parametrize("row, col", [(r, c) for r in range(3) for c in range(3)])
def test_new_board_each_cell_is_empty(board, row, col):
    assert board.cell(row, col) == EMPTY

def test_place_mark_on_empty_cell_should_succeed(board):
    assert board.place_mark(1, 0, MARK_O)
    assert board.cell(1, 0) == MARK_O
    assert (1, 0) not in board.empty_cells()

@pytest.mark.parametrize("second_mark", [MARK_X, MARK_O])
def test_taken_cell_is_rejected_and_first_mark_stays(board, second_mark):
    assert board.place_mark(0, 0, MARK_X)

    assert not board.place_mark(0, 0, second_mark)
    assert board.cell(0, 0) == MARK_X

@pytest.mark.parametrize("row, col", OFF_BOARD)
def test_off_board_place_mark_is_rejected_with_board_unchanged(board, row, col):
    before = board.empty_cells()

    assert not board.place_mark(row, col, MARK_X)
    assert board.empty_cells() == before

@pytest.mark.parametrize("row, col", OFF_BOARD)
def test_off_board_cell_raises(board, row, col):
    with pytest.raises(ValueError, match="row and col must be between 0 and 2"):
        board.cell(row, col)

def test_board_cell_is_empty_after_remove_mark(board):
    assert board.place_mark(0, 0, MARK_X)

    board.remove_mark(0, 0)

    assert board.cell(0, 0) == EMPTY
    assert (0, 0) in board.empty_cells()

def test_remove_mark_only_clears_that_cell(board):
    assert board.place_mark(0, 0, MARK_X)
    assert board.place_mark(1, 1, MARK_O)

    board.remove_mark(0, 0)

    assert board.cell(1, 1) == MARK_O
    assert (1, 1) not in board.empty_cells()

def test_remove_cell_can_be_used_again(board):
    assert board.place_mark(0, 0, MARK_X)
    board.remove_mark(0, 0)

    assert board.place_mark(0, 0, MARK_O)
    assert board.cell(0, 0) == MARK_O

def test_remove_mark_on_empty_cell_does_nothing(board):
    before = board.empty_cells()

    board.remove_mark(0, 0)

    assert board.empty_cells() == before

@pytest.mark.parametrize("row, col", OFF_BOARD)
def test_off_board_remove_mark_raises(board, row, col):
    with pytest.raises(ValueError, match="row and col must be between 0 and 2"):
        board.remove_mark(row, col)