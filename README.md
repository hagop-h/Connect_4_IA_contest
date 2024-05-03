# Project Overview
This project revolves around the implementation of a `Connect Four` game, offering diverse gameplay modes and AI difficulty levels. The primary objective is to provide an engaging and interactive gaming experience for users, incorporating strategic decision-making and dynamic gameplay elements.

# Configuration Requirements
To ensure smooth execution of the Connect Four game, the following configurations are required:
`Python Environment`: The project requires a Python environment to run the game scripts.
`Dependencies`: Ensure that all necessary dependencies, such as NumPy, are installed in the Python environment.
`Operating System Compatibility`: The game is compatible with various operating systems, including Windows, macOS, and Linux.
`Terminal or Command Prompt`: Users can run the game directly from a terminal or command prompt interface.
`Hardware Resources`: The game is lightweight and does not demand significant hardware resources, making it suitable for a wide range of systems.

## Position Class
**Purpose:** 
The Position class is central to managing the current state of a board game, enabling dynamic assessment and manipulation of the game grid. It offers a range of functionalities designed to enhance gameplay and interaction. Here’s a breakdown of its key features:

**Features:**
    -`Initialization (__init__)`: Initializes an instance with a specific grid state and the current player. This setup is essential for starting or loading a game state.
    -`Terminal State Detection (is_terminal)`: Checks whether the game has reached a terminal state, i.e., the game ends either because a player has won or because the grid is full. This function is crucial for determining game over conditions.
    -`Grid Evaluation (evaluate)`: Calculates a score for the current grid state, favoring the player 'R'. A positive score indicates an advantage for 'R', while a negative score favors 'J'. This evaluation helps in strategic decision-making, especially for AI implementations.
    -`Position-specific Evaluation (evaluate_position)`: Assesses the favorability of a specific grid position based on its proximity to a winning condition. This detailed evaluation is used to weigh the strategic importance of individual moves.
    -`Move Generation (generate_moves)`: Generates a list of all possible moves that the current player can make, based on available columns in the grid. This function is key for AI to analyze potential future moves.
    -`Move Application (play)`: Applies a move to the grid and returns the new game state with the next player. This method is essential for advancing the game after a player's decision.
    -`Winner Check (check_winner)`: Determines if a player has won the game horizontally, vertically, or diagonally. This check is critical for immediate game outcome assessments.

**Other Utilities Functions:**
The Position class includes several utility functions designed to evaluate and manipulate the game state effectively. Below are detailed descriptions of each function:

- `find_empty_row(grid, col)`: Finds the first empty row in a specified column from the bottom up, allowing for the placement of a new piece in the game.
- `count_consecutive_horizontal(grid, player, row, col)`: Counts consecutive pieces horizontally from a specified position, aiding in the evaluation of potential winning moves.
- `count_consecutive_vertical(grid, player, row, col)`: Counts consecutive pieces vertically from a specified position, crucial for assessing vertical threats in the game.
- `count_consecutive_diagonal_right(grid, player, row, col)` and `count_consecutive_diagonal_left(grid, player, row, col)`: These functions count consecutive pieces along both major diagonals from a specified position, essential for evaluating diagonal winning opportunities.
- `tie(grid)`: Checks if the game has reached a tie state where no valid moves are available.

### AI Move Decision Functions
This section describes the functions responsible for computing the AI's moves in the game based on the selected difficulty level. Each function utilizes a different strategy or complexity to match the intended game difficulty, enhancing the gameplay experience for different types of players.

- `make_ai_move(grid, player, difficulty, transposition_table=None)`: Chooses and returns the AI's move according to the difficulty level specified.
- `transposition_table`: An optional dictionary for storing evaluated positions to improve performance.

**AI moves strategies:**
- `negamax(position, alpha, beta, depth, transposition_table=None)`: Performs a recursive search using the Negamax algorithm to evaluate potential moves, optimized with alpha-beta pruning for efficiency.

- `easy_ai_move(player, grid, transposition_table=None)`: Implements the AI's strategy for 'easy' difficulty. This function is designed to make decisions quickly, using a simple heuristic and minimal depth search to provide a less challenging opponent.
- `medium_ai_move(player, grid, transposition_table=None)`: Implements a moderately challenging AI opponent by using the Minimax algorithm with moderate search depth.
- `hard_ai_move(player, grid, transposition_table=None)`: Provides a high level of challenge by employing a deep Minimax search algorithm, making it suitable for experienced players seeking a rigorous test of their skills.

####  Game Mode
**Player vs Player:**
`play_player_vs_player(grid, player, cols)`: This function enables two human players to take turns placing their respective markers on the game board until one of them wins or the game ends in a tie.

**Player vs AI:**
`play_player_vs_ai(grid, player, difficulty, cols)`: This function allows a human player to compete against an AI opponent, with the AI making moves based on the specified difficulty level. The game continues until either the human player or the AI wins or the game ends in a tie.

**AI vs AI:**
`play_ai_vs_ai(grid, player, difficulty_r, difficulty_j, cols)`: This function allows two AI opponents to compete against each other, with each AI making moves based on its specified difficulty level. The game continues until one of the AIs wins or the game ends in a tie.

**AI vs AI Game Mode with Statistics:**
`play_ai_vs_ai_stats(difficulty1, difficulty2, iterations)`: This function conducts a specified number of AI vs AI matches, recording the wins for each AI and calculating win ratios. It also measures the total execution time and average time per iteration.


##### Main Function: Play Connect Four
This function controls the main game loop and allows the player to `choose different game modes, including Player vs Player, Player vs AI, AI vs AI, and statistics mode`. It initializes the game parameters such as the grid, player, and game board dimensions. The function prompts the user to select a game mode and executes the corresponding gameplay function based on the chosen mode. It also handles `errors and exceptions` during the game execution.


**Unit Tests :**
We have integrated unit tests into our code in the file `Test_Connect4`, using pytest to ensure that any modifications do not impact other parts of the code. This approach helps maintain the integrity and functionality of the system as it evolves.