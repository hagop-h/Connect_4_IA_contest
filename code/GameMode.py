import time
import sys
from Position import Position
from UtilsPosition import tie, find_empty_row
from UtilsAiMoves import make_ai_move
from Interface import print_board

# ---------------------------------------------
# Game Mode
# ---------------------------------------------

# -----
# Player vs Player 
# -----

def play_player_vs_player(grid, player, cols):
    """
    Purpose: Facilitates a Player vs Player game mode.
    Parameters:
    - grid: A 2D list representing the game board.
    - player: Initial player ('R' or 'J').
    - cols: Number of columns in the grid.
    Details: This function enables two human players to take turns placing their respective markers on the game board
    until one of them wins or the game ends in a tie.
    """
    while True:
        if not tie(grid):
            print("La partie est un match nul.")
            break

        user_input = input(f"Joueur {player}, choisissez une colonne (0-6) pour placer votre pion: ")

        try:
            col_choice = int(user_input)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 0 et 6: ")
            continue

        if 0 <= col_choice < cols and grid[0][col_choice] == ' ':
            row_insert = find_empty_row(grid, col_choice)
            grid[row_insert][col_choice] = player
            print_board(grid)

            position = Position(grid, 'R' if player == 'J' else 'J')
            if position.check_winner():
                grid[row_insert][col_choice] = player
                print_board(grid)
                print(f"Le joueur {player} a gagné !")
                break

            player = 'J' if player == 'R' else 'R'
        else:
            print("Choix invalide. Veuillez choisir une colonne valide.")


# -----
# Player vs AI 
# -----

def play_player_vs_ai(grid, player, difficulty, cols):
    """
    Purpose: Facilitates a Player vs AI game mode.
    Parameters:
    - grid: A 2D list representing the game board.
    - player: Initial player ('R' or 'J').
    - difficulty: Difficulty level for the AI ('easy', 'medium', or 'hard').
    - cols: Number of columns in the grid.
    Details: This function allows a human player to compete against an AI opponent, with the AI making moves based on
    the specified difficulty level. The game continues until either the human player or the AI wins or the game ends in a tie.
    """
    while True:
        if not tie(grid):
            print("La partie est un match nul.")
            break

        if player == 'R':
            user_input = input(f"Joueur {player}, choisissez une colonne (0-6) pour placer votre pion : ")

            try:
                col_choice = int(user_input)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entre 0 et 6 ")
                continue

            if 0 <= col_choice < cols and grid[0][col_choice] == ' ':
                row_insert = find_empty_row(grid, col_choice)
                grid[row_insert][col_choice] = player
                print_board(grid)

                position = Position(grid, 'R' if player == 'J' else 'J')
                if position.check_winner():
                    grid[row_insert][col_choice] = player
                    print_board(grid)
                    print(f"Le joueur {player} a gagné !")
                    break

                player = 'J'
            else:
                print("Choix invalide. Veuillez choisir une colonne valide.")
        else:
            col_choice = make_ai_move(grid, player, difficulty)
            print(f"L'IA a choisi la colonne {col_choice}")

            if col_choice == -2:
                print("La partie est un match nul.")
                break

            if 0 <= col_choice < cols and grid[0][col_choice] == ' ':
                row_insert = find_empty_row(grid, col_choice)
                grid[row_insert][col_choice] = player
                print_board(grid)

                position = Position(grid, 'R' if player == 'J' else 'J')
                if position.check_winner():
                    grid[row_insert][col_choice] = player
                    print_board(grid)
                    print(f"Le joueur {player} a gagné !")
                    break

                player = 'R'
            else:
                print("L'IA a choisi une colonne invalide. Le jeu continue.")


# -----
# AI vs AI 
# -----

def play_ai_vs_ai(grid, player, difficulty_r, difficulty_j, cols):
    """
    Function to facilitate an AI vs AI game mode.
    
    Parameters:
    - grid: A 2D list representing the game board.
    - player: Initial player ('R' or 'J').
    - difficulty_r: Difficulty level for player Rouge's AI ('easy', 'medium', or 'hard').
    - difficulty_j: Difficulty level for player Jaune's AI ('easy', 'medium', or 'hard').
    - cols: Number of columns in the grid.
    
    Details: This function enables two AI opponents to play against each other. It alternates between the AI players' turns, making moves based on their specified difficulty levels until one of them wins or the game ends in a tie.
    """
    while True:
        if player == 'R':
            # Player Rouge's turn
            col_choice = make_ai_move(grid, player, difficulty_r)
            print(f"L'IA du joueur Rouge a choisi la colonne {col_choice}")
        else:
            # Player Jaune's turn
            col_choice = make_ai_move(grid, player, difficulty_j)
            print(f"L'IA du joueur Jaune a choisi la colonne {col_choice}")

        # Check if there are no valid moves left, resulting in a tie
        if col_choice == -2:
            print("La partie est un match nul.")
            break

        # Check if the chosen column is within the bounds of the grid and is not full
        if 0 <= col_choice < cols and grid[0][col_choice] == ' ':
            # Find the empty row to place the player's piece in the chosen column
            row_insert = find_empty_row(grid, col_choice)
            # Place the player's piece in the grid
            grid[row_insert][col_choice] = player
            # Display the updated game board
            print_board(grid)

            position = Position(grid, 'R' if player == 'J' else 'J')
            # Check if the current player has won after placing their piece
            if position.check_winner():
                grid[row_insert][col_choice] = player  # Keep the winning move on the board
                print_board(grid)  # Display the final board state
                print(f"Le joueur {player} a gagné !")  # Print the winning message
                break

            player = 'J' if player == 'R' else 'R'  # Switch to the other player's turn
        else:
            print(f"L'IA a choisi une colonne invalide. Le jeu continue.")

# ----------------------------------------------------
# Calculates statistics for multiple AI vs AI matches 
# ----------------------------------------------------

def play_ai_vs_ai_stats(difficulty1, difficulty2, iterations):
    """
    Function to play AI vs AI multiple times and calculate statistics.
    
    Parameters:
    - difficulty1: Difficulty level for the first AI ('easy', 'medium', or 'hard').
    - difficulty2: Difficulty level for the second AI ('easy', 'medium', or 'hard').
    - iterations: Number of iterations (matches) to play.
    
    Details: This function conducts a specified number of AI vs AI matches, recording the wins for each AI and calculating win ratios. It also measures the total execution time and average time per iteration.
    """
    wins1 = 0
    wins2 = 0
    start_time = time.time()  # Start the timer

    for i in range(iterations):
        # Display the progress bar
        normalized_score = (i+1) / iterations
        bar_length = 20
        filled_length = int(normalized_score * bar_length)
        filled_char = '█'
        empty_char = '░'
        progress_bar = filled_char * filled_length + empty_char * (bar_length - filled_length)
        sys.stdout.write(f'\r Loading : [{progress_bar}] {int(normalized_score * 100)}%')
        sys.stdout.flush()

        grid = [[' ' for _ in range(7)] for _ in range(6)]  # Initialize the game grid
        player = 'R'  # Player Rouge starts the game

        while True:
            if player == 'R':
                col_choice = make_ai_move(grid, player, difficulty1)  # AI 1's turn
            else:
                col_choice = make_ai_move(grid, player, difficulty2)  # AI 2's turn

            if col_choice == -2:
                break  # No valid moves left, end the game

            row_insert = find_empty_row(grid, col_choice)
            grid[row_insert][col_choice] = player

            position = Position(grid, 'R' if player == 'J' else 'J')
            if position.check_winner():
                if player == 'R':
                    wins1 += 1
                else:
                    wins2 += 1
                break

            player = 'J' if player == 'R' else 'R'  # Switch player

    sys.stdout.write('\n')  # Move to a new line after the progress bar
    end_time = time.time()  # Stop the timer
    total_time = end_time - start_time  # Calculate total execution time
    average_time = total_time / iterations  # Calculate average time per iteration

    ratio1 = wins1 / iterations
    ratio2 = wins2 / iterations

    print(f"Nombre de victoires pour le premier IA ({difficulty1}): {wins1}")
    print(f"Nombre de victoires pour le deuxième IA ({difficulty2}): {wins2}")
    print(f"Ratio de victoires pour le premier IA: {ratio1}")
    print(f"Ratio de victoires pour le deuxième IA: {ratio2}")
    print(f"Temps d'exécution total : {total_time:.2f} secondes.")
    print(f"Temps moyen par itération : {average_time:.2f} secondes.")