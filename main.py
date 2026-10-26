"""
Tic Tac Toe Game: Start the game which takes user input and runs the game
until we have a winner or a draw.
The game is a 3x3 board where the players take turns to mark (X or O) in empty cells.
the first player to get 3 marks in a row (across, down or diagonally) wins the game. 
If all cells are filled and no player has 3 marks in a row, the game ends in a draw.
"""

from board import Board
from game import Game

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
    """Return the board as text."""
    size = board.size

    divider = "+".join(["---"] * size)
    lines = []

    for row in range(size):
        if row:
            lines.append(divider)
        cells = "|".join(f" {board.cell(row, col)} " for col in range(size))
        lines.append(f"{cells}")

    return "\n".join(line.rstrip() for line in lines)

def play_game(game: Game, read=input, write=print) -> None:
    """Run game to the end, reading moves with read and 
    showing moves with write.
    """
    while not game.is_over:
        text = read(f"{game.current_player}'s move (row col): ")
        try:
            row, col = parse_move(text, game.board.size)
        except ValueError as error:
            # diplay the error, skip next part of code
            # continue asking the input for same player
            write(str(error))
            continue

        if not game.take_turn(row, col):
            # invalid choice again, skip remining part of code
            # continue asking for same player's input
            write("That cell is already taken.")
            continue

        # display game state
        write(render_board(game.board))

    if game.winner:
        write(f"{game.winner} wins!")
    else:
        write("It's a draw.")

def main() -> None:
    play_game(Game())

if __name__ == "__main__":
    main()