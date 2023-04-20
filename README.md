# Tic-Tac-Toe Game in Python

This is a simple implementation of the classic Tic-Tac-Toe game in Python. In this game, the machine will always play a move at a random location on the board.
The game can be played as "Player vs Player" or "Player vs Machine"

## How to Play

1. Clone this repository to your local machine.
2. Navigate to the directory where the repository was cloned.
3. Run `python tic_tac_toe.py` on your command prompt/terminal.
4. The game will ask you the game mode. 
5. The game will start, and you will be asked to make your first move.
6. The machine will make its move, and the game will continue until a player wins or the board is full.

## Features

- The game is played on a simple command-line interface.
- The game supports PvP mode
- The machine makes a random move each turn.

## Functions Used

The following functions are used in the implementation of this game:

- `display_board()`: Displays the Tic-Tac-Toe board on the command-line interface.
- `play_game()`: The main function that handles the game logic and flow.
- `handle_turn(player)`: Handles the player's turn and places their move on the board.
- `check_rows()`, `check_columns()`, `check_diagonals()`: Helper functions that check the board for a win condition.

## Contributing

Contributions are always welcome! If you have any suggestions or corrections to make, feel free to open an issue or a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
