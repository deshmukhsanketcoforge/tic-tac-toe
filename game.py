"""
Game module: contains the main logic of game and functions to check 
for winner and draw.
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
        """Return True if the board is full and nobody has won."""
        return self._winner is None and self._board.is_full()

    @property
    def board(self) -> Board:
        """Return the board. Callers must only read from it."""
        return self._board

    def take_turn(self, row: int, col: int) -> bool:
        """Place the current player's mark at row, col (counting from 0).

        Return True if the move was made.
        Return False, and keep the same player's turn, if the cell is taken or
        off the board, or the game is already over.
        """
        if self.is_over:
            return False

        if not self._board.place_mark(row, col, self._current):
            return False

        if self._board.has_won(self._current):
            self._winner = self._current
        else:
            self._current = MARK_O if self._current == MARK_X else MARK_X

        return True
