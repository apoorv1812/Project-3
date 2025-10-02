✨ Features
Two-Player Mode: Allows two users to play against each other locally.

Player Setup: Prompts players for their names and allows them to choose their respective markers ('X' or 'O').

Visual Board Representation: Displays the 3x3 game board using numbers (1-9) to indicate available move locations.

Win Detection: Includes logic to check for horizontal, vertical, and diagonal win conditions after every move.

🚀 How to Run the Game
Prerequisites
You only need a modern Python environment installed on your system.

Steps
Save the Code: Ensure the Python code is saved in a file named tic_tac_toe.py.

Open Terminal: Navigate to the directory containing tic_tac_toe.py using your command prompt or terminal.
(Based on your previous terminal output, this location is likely C:\Users\APOORV\OneDrive\Desktop\extra\python\Project 3_1)

Execute the Script: Run the game using the Python interpreter:

python tic_tac_toe.py

🕹️ Game Instructions
The game proceeds as follows:

Start: The game will greet you and ask for Player 1 and Player 2 names.

Marker Selection: Each player will choose their marker ('O' or 'X').

Note: Your current implementation determines which player goes first based on who selects 'O'.

Making a Move: The current board state will be printed. Players input the number (1-9) corresponding to the cell where they want to place their marker.

[1, 2, 3] corresponds to the top row.

[4, 5, 6] corresponds to the middle row.

[7, 8, 9] corresponds to the bottom row.

Winning: The game will announce the winner if a player successfully gets three of their markers in a row (horizontal, vertical, or diagonal).
