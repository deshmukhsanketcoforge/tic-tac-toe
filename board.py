"""
Board module: contains the Board class which represents the game board and
its state.
It provides methods to update the board state and check for valid moves.
"""

EMPTY = " "

class Board:
    def __init__(self, size = 3):
        if size < 3:
            raise ValueError("size must be at least 3")
        self._size = size
        self._grid = [[EMPTY] * self.size for _ in range(self.size)]

    @property
    def size(self):
        return self._size