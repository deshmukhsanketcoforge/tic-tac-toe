"""
AI module: compugter players. Each one is asked a move through 
choose_move, so the game never needs to know which level it is playing.
"""

import random

from abc import ABC, abstractmethod
from board import Board, MARK_O, MARK_X

class AIPlayer(ABC):
    """Base class for computer players."""

    def __init__(self, rng: random.Random) -> None:
        self._rng = rng

    @abstractmethod
    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        """Return the (row, col) mark should play next.

        The board must have an empty cell, and is left unchanged.
        """

class EasyAI(AIPlayer):
    """Plays a random empty cell."""

    def choose_move(self, board: Board, mark: str) -> tuple[int, int]:
        return self._rng.choice(board.empty_cells())

class HardAI(AIPlayer):
    """Plays best move find by minimax, so it never loses."""

    def _score(self, board: Board, me: str, opponent: str, to_move: str, depth: int) -> int:
        """Score the board for me, assuming both sidesplay their best.
        
        A quicker win scores higher and a quicker loss scores lower.
        """

        # if won == me, +ve score, else -ve score
        if board.has_won(me):
            return 10 - depth   # max depth is 9 on board of 3x3

        if board.has_won(opponent):
            return depth - 10

        if board.is_full():
            return 0

        next_to_move = opponent if to_move == me else me
        scores = []
        for row, col in board.empty_cells():
            board.place_mark(row, col, to_move)
            scores.append(
                self._score(board, me, opponent, next_to_move, depth + 1)
            )
            board.remove_mark(row, col)

        return max(scores) if to_move == me else min(scores)
    
    def choose_move(self, board: Board, mark: str):
        opponent = MARK_O if mark == MARK_X else MARK_X

        best_score = None
        best_moves = []

        for row, col in board.empty_cells():
            board.place_mark(row, col, mark)
            score = self._score(board, mark, opponent, opponent, 1)
            board.remove_mark(row, col)

            if best_score is None or score > best_score:
                best_score, best_moves = score, [(row, col)]
            elif score == best_score:
                best_moves.append((row, col))


        return self._rng.choice(best_moves)