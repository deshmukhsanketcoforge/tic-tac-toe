import pytest

from board import MARK_O, MARK_X
from game import Game

@pytest.fixture
def game():
    """A fresh game."""
    return Game()

def test_new_game_starts_with_x(game):
    assert game.current_player == MARK_X

def test_new_game_has_no_winner_and_is_not_over(game):
    assert game.winner is None
    assert not game.is_draw
    assert not game.is_over

