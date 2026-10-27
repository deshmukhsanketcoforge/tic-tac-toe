"""
Tic Tac Toe Game: Start the game which takes user input and runs the game
until we have a winner or a draw.
The game is a 3x3 board where the players take turns to mark (X or O) in empty cells.
the first player to get 3 marks in a row (across, down or diagonally) wins the game.
If all cells are filled and no player has 3 marks in a row, the game ends in a draw.
"""

import random

from board import Board, MARK_O
from game import Game
from ai import AIPlayer, EasyAI, HardAI

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

def play_game(game: Game, read=input, write=print,
              ai: AIPlayer | None = None) -> None:
    """Run game to the end.

    Moves are read with read and everything is shown with write.
    If ai is given, it plays O and the human plays X.
    """
    # Display initial board
    write(render_board(game.board))

    while not game.is_over:
        if ai is not None and game.current_player == MARK_O:
            row, col = ai.choose_move(game.board, MARK_O)
            game.take_turn(row, col)
            write(f"Computer plays {row + 1} {col + 1}")
            write(render_board(game.board))
            continue


        text = read(f"{game.current_player}'s move (row col): ")
        try:
            row, col = parse_move(text, game.board.size)
        except ValueError as error:
            # display the error, skip next part of code
            # continue asking the input for same player
            write(str(error))
            continue

        if not game.take_turn(row, col):
            # invalid choice again, skip remaining part of code
            # continue asking for same player's input
            write("That cell is already taken.")
            continue

        # display game state
        write(render_board(game.board))

    if game.winner:
        write(f"{game.winner} wins!")
    else:
        write("It's a draw.")

def ask_choice(prompt: str, options: list[str],
               read=input, write=print) -> str:
    """Ask until the answer is one of options, and return it."""
    while True:
        answer = read(prompt).strip()
        if answer in options:
            return answer
        write(f"Please enter one of: {','.join(options)}")

def choose_opponent(rng: random.Random, read=input,
                    write=print) -> AIPlayer | None:
    """Ask for the mode.

    Return None for two players, or the AI to play O.
    """
    mode = ask_choice("Mode - 1: two players, 2: versus computer: ",
                      ["1", "2"], read, write)
    if mode == "1":
        return None

    level = ask_choice("Difficulty - 1: easy, 2: hard: ",
                       ["1", "2"], read, write)

    return EasyAI(rng) if level == "1" else HardAI(rng)

def main() -> None:
    ai = choose_opponent(random.Random())
    play_game(Game(), ai=ai)

if __name__ == "__main__":
    main()
