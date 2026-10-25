"""
Game module: containes the main logic of game and functions to check for winner and draw.
"""

from board import Board, MARK_O, MARK_X

class Game:
    """A game on a board. X always goes first then players alternate."""
    def __init__(self) -> None:
        self._board = Board()
        self._current = MARK_X
        self._winner = None

    @property
    def is_over(self) -> bool:
        """Return True if someone has won or the game is a draw."""
        return self._winner is not None or self._board.is_full()

    @property
    def current_player(self) -> str:
        """Return the mark of the current player."""
        return self._current

    @property
    def winner(self) -> str | None:
        """Return the winning mark, or None if nobody has won."""
        return self._winner

    @property
    def is_draw(self) -> bool:
        """Return true if the board is full and nobody has won."""
        return self._winner is None and self._board.is_full()