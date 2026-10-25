"""
Board module: contains the Board class which represents the game board and
its state.
It provides methods to update the board state and check for valid moves.
"""

EMPTY: str = " "
MARK_X: str = "X"
MARK_O: str = "O"

class Board:
    def __init__(self, size: int = 3) -> None:
        if size < 3:
            raise ValueError("size must be at least 3")
        self._size = size
        self._grid = [[EMPTY] * self.size for _ in range(self.size)]

    @property
    def size(self) -> int:
        return self._size

    def cell(self, row: int, col: int) -> str:
        """Return the mark at row, col (counting from 0).

        Raise ValueError if row, col is off the board.
        """
        if not self._in_range(row, col):
            raise ValueError(f"row and col must be between 0 and {self.size - 1}")
        return self._grid[row][col]

    def _in_range(self, row: int, col: int) -> bool:
        """Return True if row and col are both on the board."""
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row: int, col: int, mark: str) -> bool:
        """Place mark at given row, col.

        Return True if placed, False if the cell is taken or off the board.
        """
        if not self._in_range(row, col):
            return False
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def empty_cells(self) -> list[tuple[int, int]]:
        """Return a list of (row, col) pairs for every empty cell."""
        return [(r, c) for r in range(self._size) for c in range(self._size)
                if self._grid[r][c] == EMPTY]
