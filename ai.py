"""
AI module: compugter players. Each one is asked a move through 
choose_move, so the game never needs to know which level it is playing.
"""

import random

from abc import ABC, abstractmethod
from board import Board

class AIPlayer(ABC):
    """Base class for computer players."""

    def __init__(self, rng: random.Random) -> None:
        self._rng = rng

    @abstractmethod
    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return the (row, col) mark should play next.

        The board must have an empty cell, and is left unchanged.
        """