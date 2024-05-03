from AiMoves import easy_ai_move, medium_ai_move, hard_ai_move

# -----
# AI Move Decision Functions
# -----

def get_valid_difficulty(prompt):
    """
    Prompts the user to input a valid difficulty level for the game.
    Parameters:
    - prompt: String prompt displayed to the user.
    Returns:
    - The chosen difficulty level as a string if valid ('easy', 'medium', 'hard').
    """
    while True:
        difficulty = input(prompt)
        if difficulty.lower() in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Erreur : Niveau de difficulté invalide. Veuillez choisir parmi 'easy', 'medium' ou 'hard'.")


def make_ai_move(grid, player, difficulty, transposition_table=None):
    """
    Determines the AI's move based on the selected difficulty level.
    Parameters:
    - grid: 2D list representing the game board.
    - player: Character representing the AI player.
    - difficulty: String indicating the difficulty level ('easy', 'medium', 'hard').
    - transposition_table: Dictionary used to store already evaluated game states, enhancing efficiency.
    Returns:
    - Integer representing the column index for the AI's move or -2 if no valid moves are available.
    """
    if transposition_table is None:
        transposition_table = {}

    valid_columns = [col for col in range(len(grid[0])) if grid[0][col] == ' ']
    if not valid_columns:
        return -2  # Indicates a tie or no valid moves available

    # Select move based on difficulty
    if difficulty == "easy":
        return easy_ai_move(player, grid)
    elif difficulty == "medium":
        return medium_ai_move(player, grid, transposition_table)
    elif difficulty == "hard":
        return hard_ai_move(player, grid, transposition_table)
