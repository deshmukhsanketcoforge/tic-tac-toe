# tic-tac-toe

A classic game played between 2 players with markers (X and O), X goes first. Each turn the player picks a cell to place the marker. The game stops when it's a draw (no empty cells left) or when there is a winner.

Game accepts space separated 2 whole numbers as row and column. Other inputs are rejected.

> Player does not lose their turn for incorrect input, they get another chance.

Examples of invalid input:
1. Input with only 1 number
2. Input with empty string
3. Input with more than 2 numbers
4. Input with at least one floating number
5. Input with string
6. Input with numbers beyond range (1, size)
7. Input with a cell already taken

## Game modes

At the start the game asks for a mode:

1. **Two players**: X and O take turns on the same terminal.
2. **Versus computer**: you play X and the computer plays O. Then choose the difficulty:
   1. **Easy**: the computer picks a random empty cell.
   2. **Hard**: the computer uses the minimax algorithm and never loses when it plays second.

An invalid menu answer is rejected and the question is asked again.

## Project structure

```
tic-tac-toe/
├── .github/
│   └── workflows/
│       └── ci.yml          # runs pytest on pull requests and on main
├── tests/
│   ├── test_ai.py          # AI players: seeded Easy, Hard minimax
│   ├── test_board.py       # Board rules: marks, off-board, win, draw
│   ├── test_game.py        # turn order, win and draw detection
│   └── test_main.py        # move parsing, board rendering, menu, game loop
├── ai.py                   # AIPlayer base class, EasyAI and HardAI
├── board.py                # Board class (3x3 grid, marks, win and full checks)
├── game.py                 # Game class (turns, winner, draw)
├── main.py                 # menu, prompts and display (the only file that prints and reads input)
├── conftest.py             # lets pytest import the modules from the root
├── requirements.txt        # pinned packages (pytest)
├── PLAN.md                 # plan: goal, requirements, components, decisions
└── README.md               # how to run the game and the tests
```

## Requirements

Python 3.10 or later.

## Setup

1. Clone the repository and open it in a terminal.
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
3. Install the packages:
   ```
   pip install -r requirements.txt
   ```

## How to run the game

```
python main.py
```

Choose the game mode (and the difficulty, if you play the computer), then
enter a move as a row and a column, counting from 1, for example `2 3`
(second row, third column). X goes first.

## How to run the tests

```
pytest
```


## Contributors

Sanket Deshmukh

> Note: This project was developed as part of assignment given at Momentuum Blue (A Coforge Company).
