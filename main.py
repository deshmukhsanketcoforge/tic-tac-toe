"""
Tic Tac Toe Game: Start og the game which takes user input and runs the game
until we have a winner or a draw.
The game is a 3x3 board where the players take turns to mark (X or O) in empty cells.
the first player to get 3 marks in a row (acroos, down or diagonally) wins the game. 
If all cells are filled and no player has 3 marks in a row, the game ends in a draw.
"""

from board import Board

NOT_NUMBERS = "Enter a row and a column as two numbers, like: 2 3"

def parse_move(text: str, size: int) -> tuple[int, int]:
    """Turn the player's "row col" (counting from 1) into 0-based (row, col).
    
    Raise ValueError with a message for the player if text is not
    two whole numbers, or a number is outside range (1, size).
    """
    parts = text.split()

    if len(parts) != 2:
        raise ValueError(NOT_NUMBERS)
    
    try:
        row, col = int(parts[0]), int(parts[1])
    except ValueError:
        raise ValueError(NOT_NUMBERS) from None

    if not (1 <= row <= size and 1 <= col <= size):
        raise ValueError(f"Row and column must be between 1 and {size}")

    return row - 1, col - 1

def render_board(board: Board) -> str:
    """Return the board as text, with row and column numbers from 1."""
    size = board.size

    divider = "+".join(["---"] * size)
    lines = []

    for row in range(size):
        if row:
            lines.append(divider)
        cells = "|".join(f" {board.cell(row, col)} " for col in range(size))
        lines.append(f"{cells}")

    return "\n".join(line.rstrip() for line in lines)