# Tic-Tac-Toe Game

A Python implementation of the classic Tic-Tac-Toe game with both human vs human and human vs computer gameplay modes, featuring a graphical user interface.

## Features

- **Two Game Modes:**
  - Human vs Human (game_type = 1)
  - Human vs AI (game_type = 2)
- **Graphical Interface:** Visual board display using a custom GUI
- **AI Opponent:** Intelligent computer player with strategic decision-making
- **Input Validation:** Robust move validation and error handling
- **Win Detection:** Automatic winner detection for rows, columns, and diagonals

## Project Timeline
- **Start Date:** August 2023
- **Completed:** August 2023

## Installation

1. Ensure you have Python 3 installed
2. Install pygame:
   ```bash
   pip install pygame
   ```
3. Make sure the required custom modules (`stdarray`, `stdio`, `Gui`) are in your Python path

## Usage

Run the game from the command line with a game type argument:

```
python TicTacToe.py <game_type>
```

Where `<game_type>` is:
- `1` for Human vs Human
- `2` for Human vs AI

### Example:
```bash
python TicTacToe.py 1  # Human vs Human
python TicTacToe.py 2  # Human vs AI
```

## How to Play

1. The game displays a 3x3 board numbered 1-9
2. Players take turns entering moves by typing the number (1-9) corresponding to their desired position
3. Player 1 uses 'X' and Player 2 (or AI) uses 'O'
4. The first player to get three in a row (horizontally, vertically, or diagonally) wins
5. The game displays the winner and shows the final board state

### Board Layout:
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## AI Strategy

The AI opponent uses a strategic approach with the following priority order:

1. **Winning Move:** Takes any move that results in an immediate win
2. **Blocking Move:** Blocks the human player from winning on their next turn
3. **Adjacent Move:** Looks for moves adjacent to existing 'O' pieces
4. **Strategic Positioning:** Attempts to find clear rows for future wins
5. **Random Move:** Falls back to a random valid move if no strategic move is found
