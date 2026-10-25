import pytest

from board import Board

@pytest.fixture
def board():
    """A fresh, empty 3x3 board for each test."""
    return Board()

def test_board_smaller_than_3_is_rejected():
    with pytest.raises(ValueError, match="size must be at least 3"):
        Board(2)

def test_board_size_returns_actual_size(board):
    assert board.size == 3