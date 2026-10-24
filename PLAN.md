## Goal

1. Tic-tac-toe is a two player game, where each player is assigned a mark 'X' or 'O'. Each player takes alternate turn and game ends with win or draw.
2. The game runs in the terminal and can be played between two people or between one person and the computer. 

## Requirements


| Id | Requirement | How will I verify it? |
|----|-------------|-----------------------|
| 1 | Board should be of size 3x3 |  A new Board's empty_cells() returns exactly the 9 (row, col) pairs for rows and columns 0-2. place_mark succeeds at (0,0) and (2,2) and fails at (3,3) |
| 2 | X always goes first | In game.py, a new game's current player is X; after one valid move it becomes O, and marks keep alternating |
| 3 | Row or column typed by the player in 1-3 is accepted | main.py converts 1-based input to 0-based in one place: test that "1 1" gives (0,0) and "3 3" gives (2,2). On the Board, place_mark returns True at 0 and 2 |
| 4 | Row or column outside 1-3 is rejected | Parsing "0 1" and "4 4" is rejected with a message. On the Board, place_mark returns False for -1 and 3 in either position and the board is unchanged |
| 5 | The game detects a win | For each of the 8 lines (3 rows, 3 columns, 2 diagonals) and for both X and O, fill the line and verify has_won(mark) is True. Also verify it is False for incomplete lines and for the other mark |
| 6 | The game detects a draw | Fill the board with no three in a row: is_full() is True and has_won is False for both marks. A last move that fills the board and completes a line is a win, not a draw |
| 7 | Easy pick a random cell | Verify the cell picked in Easy mode (using seeding) is empty |
| 8 | Hard AI never loses on 3x3 when it plays second | HardAI plays O. A test enumerates every possible X move at each turn, with HardAI replying through choose_move, and asserts X never has_won in any game |
| 9 | Non-numeric input should show a clear message | The parsing function in main.py (no print or input inside it) rejects input such as "a b" or "2" with a message, and the game loop re-prompts the same player without losing the turn |
| 10 | A taken cell should be rejected for any update | Place a mark on a taken cell and verify if it gets rejected |
| 11 | Invalid move should not use up the turn | Perform invalid move (out of bound index, taken cell, etc.), the move should be rejected with clear message and turn shouldn't be used |
| 12 | In versus computer mode, human uses X and computer uses O | Choose computer mode and use human input with mark X, verify if computer plays second and uses mark O |
| 13 | Board should print after every move | main.py has a function that returns the board as a string (no print inside), and the game loop prints it after each move. Test that the string matches the expected board state |
| 14 | Abstract AI class can't be instantiated | Write a test that creates an instance of the abstract class and verify it raises TypeError |
| 15 | Hard AI takes a winning move when one exists | A winning move does not always exist, but when it does HardAI must pick one. Set up a board where O can win in one move, and verify HardAI's choose_move is a cell that wins |
| 16 | choose_move leaves the board unchanged | For EasyAI and HardAI, copy the board state before calling choose_move and verify it is identical afterwards |
| 17 | At start the player chooses two players or versus computer, and Easy or Hard | A menu function in main.py maps the choices to the game setup (two humans, or human X vs EasyAI/HardAI O). Invalid menu input re-prompts |

## Components

| # | Class/File | Responsibility |
|---|------------|----------------|
| 1 | board.py | Board class holds the private 3x3 grid and exposes it only through methods to place or remove a mark, list empty cells, and report a win or a full board; it never prints or tracks turns |
| 2 | ai.py: AI base class | Abstract base class (abc) that declares choose_move(board, mark) so the game can call any AI without knowing its level |
| 3 | ai.py: EasyAI, HardAI | Subclasses created with a random.Random object; EasyAI picks a random empty cell and HardAI picks a move using minimax |
| 4 | game.py | Owns turn order, mode setup and win or draw checks; it does not print or read input |
| 5 | main.py | The only place that uses print() and input(): menus, prompts and board display, and the only place that converts the player's 1-based numbers to 0-based |
| 6 | tests/ | Contains all the test cases used for applications testing |

## Decisions

| # | Options | Decision | Reason |
|---|---------|----------|--------|
| 1 | Declare draw when we can't achieve any win state from current board state OR let the players play entire game |Play full game even if draw is guaranteed | To determine draw, we need to consider all possible future board state, to see if any win state is possible, which is time consuming. Instead we can just let the user play full game and after each move, call has_won(mark), which only checks the 8 lines (3 rows, 3 columns, 2 diagonals) |
| 2 | HardAI uses predefined state mapping to guarantee a win or hardAI explore future possible states based on current choice and picks the best one | Hard AI, explores all possible future states, to determine which move will lead to win of AI, then picks the move which could lead to win | Hard AI should not lose, so it can't just randomly pick any cell, it should explore future possibilities to determine current move. A predefined mapping of board states would have to be written and checked by hand and takes more space, while exploring future states works for any position and is what the spec asks for (minimax) |
