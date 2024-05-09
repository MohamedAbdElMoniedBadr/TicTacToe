# Tic Tac Toe Game Documentation

## Overview

This project is a simple Tic Tac Toe game implemented using the Pygame library in Python. The game includes a player-vs-computer mode with an AI algorithm based on the Minimax algorithm. Additionally, the game utilizes the NumPy library for efficient array operations.

## Features

- **Player-vs-Computer Mode**: Enables a player to play against an AI opponent using the Minimax algorithm.
- **Graphics Interface**: Utilizes Pygame to create a graphical interface for the game.
- **Winning Detection**: Detects winning combinations and declares the winner accordingly.

## Installation

1. Clone the repository:https://github.com/MohamedAbdElMoniedBadr/TicTacToe
2. Navigate to the project directory:cd edit/main
3. Install the required Python libraries: pip install pygame numpy


## Usage

1. Run the main script to start the game
2. Choose the game mode:
- Player-vs-Computer: Play against the AI opponent.

3. Follow the prompts to make your moves by clicking on the grid cells.

## Implementation Details

### Pygame

The Pygame library is used to create the graphical interface of the game, including the game window, grid display, player tokens, and user interactions.

### Minimax Algorithm

The AI opponent in the player-vs-computer mode uses the Minimax algorithm to determine the optimal move. The algorithm recursively evaluates possible future game states and chooses the move that leads to the highest chance of winning or preventing the opponent from winning.

### NumPy

NumPy is used to efficiently handle the game board as a 2D array and perform array operations for game logic, such as checking for winning combinations and updating the game state.

## Customization

Feel free to customize the game by modifying the code to add new features, improve the user interface, or tweak the AI algorithm. Experiment with different strategies for the AI opponent or enhance the visual design of the game.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, new features, or bug fixes, please submit a pull request or open an issue on GitHub.









