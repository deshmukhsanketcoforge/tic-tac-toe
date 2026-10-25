import pytest

from board import Board

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

def test_new_board_has_no_marks(board):
    assert board.empty_cells() == [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

