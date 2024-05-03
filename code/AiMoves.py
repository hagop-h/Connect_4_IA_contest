import random
from UtilsPosition import find_empty_row
from Position import Position

# --------------------------------------------------
#  Negamax Algorithm for Move Evaluation
# --------------------------------------------------

def negamax(position, alpha, beta, depth, transposition_table=None):
    """
    Performs the Negamax search algorithm recursively to find the best move, optimized with alpha-beta pruning.
    Parameters:
    - position: An instance of Position class representing the current game state.
    - alpha: Alpha value for alpha-beta pruning, representing the minimum score that the maximizing player .
    - beta: Beta value for alpha-beta pruning, representing the maximum score that the minimizing player.
    - depth: The current depth in the search tree.
    - transposition_table: An optional dictionary to store previously calculated scores of positions to avoid redundant calculations.
    Returns:
    - The best score that can be achieved from the current position given optimal play.
    """
    if transposition_table is None:
        transposition_table = {}

    # Early termination if the position is a terminal state or the depth limit is reached
    if position.is_terminal() or depth == 0:
        return position.evaluate() if position.current_player == 'R' else -position.evaluate()

    # Retrieve the score from transposition table if already evaluated
    position_key = tuple(map(tuple, position.grid))
    if position_key in transposition_table:
        return transposition_table[position_key]

    valid_moves = position.generate_moves()
    # Sort moves based on heuristics for better pruning
    valid_moves.sort(key=lambda col: -position.evaluate_position(find_empty_row(position.grid, col), col))

    for move in valid_moves:
        child = position.play(move)
        score = -negamax(child, -beta, -alpha, depth - 1, transposition_table)

        # Update alpha if a better move has been found
        alpha = max(alpha, score)
        # Beta cutoff
        if score >= beta:
            return beta

    transposition_table[position_key] = alpha
    return alpha

# ---------------------------------------------
# Managinng difficulty level 
# ---------------------------------------------

# -----
# Easy Difficulty AI Move Decision
# -----
def easy_ai_move(player, grid, transposition_table=None):
    """
    AI move calculation for 'easy' difficulty using a simple heuristic.
    Parameters:
    - player: Character representing the AI player.
    - grid: 2D list representing the game board.
    - transposition_table: Dictionary for storing game state evaluations, optional.
    Returns:
    - Integer representing the column index of the chosen move or -2 if no moves are available.
    """
    if transposition_table is None:
        transposition_table = {}

    valid_columns = [col for col in range(len(grid[0])) if grid[0][col] == ' ']
    if not valid_columns:
        return -2  # No valid moves

    best_score = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    for col in valid_columns:
        row_insert = find_empty_row(grid, col)
        grid[row_insert][col] = player  # Make the move

        position_key = tuple(map(tuple, grid))  # Generate a unique key for the current grid state

        if position_key in transposition_table:
            score = transposition_table[position_key]
        else:
            position = Position(grid, 'R' if player == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, depth=3, transposition_table=transposition_table)
            transposition_table[position_key] = score  # Store the score in transposition table

        grid[row_insert][col] = ' '  # Undo the move

        if score > best_score:
            best_score = score
            best_move = col
        elif score == best_score:
            if random.random() < 0.08:  # Introduce randomness
                best_move = col

        alpha = max(alpha, score)

        if alpha >= beta:
            break

    return best_move


# -----
# Medium Difficulty AI Move Decision
# -----

def medium_ai_move(player, grid, transposition_table=None):
    """
    Calculates the AI's move at a medium difficulty level using the Minimax algorithm.
    Parameters:
    - player: Character representing the AI player.
    - grid: 2D list representing the game board.
    - transposition_table: Optional dictionary to store already evaluated game states for efficiency.
    Returns:
    - Integer representing the column index for the AI's move or -2 if no valid moves are available.
    """
    if transposition_table is None:
        transposition_table = {}

    valid_columns = [col for col in range(len(grid[0])) if grid[0][col] == ' ']
    if not valid_columns:
        return -2  # Indicates a tie or no valid moves available

    best_score = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    for col in valid_columns:
        row_insert = find_empty_row(grid, col)
        grid[row_insert][col] = player  # Make the move

        position_key = tuple(map(tuple, grid))  # Generate a unique key for the current grid state

        if position_key in transposition_table:
            score = transposition_table[position_key]
        else:
            position = Position(grid, 'R' if player == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, depth=5, transposition_table=transposition_table)
            transposition_table[position_key] = score  # Store the score

        grid[row_insert][col] = ' '  # Undo the move

        if score > best_score:
            best_score = score
            best_move = col

        alpha = max(alpha, score)

        if alpha >= beta:
            break

    return best_move


# -----
# Hard Difficulty AI Move Decision
# -----

def hard_ai_move(player, grid, transposition_table=None):
    """
    Determines the AI's move at a hard difficulty level using a deep Minimax algorithm.
    Parameters:
    - player: Character representing the AI player.
    - grid: 2D list representing the game board.
    - transposition_table: Optional dictionary to store already evaluated game states for efficiency.
    Returns:
    - Integer representing the column index for the AI's move or -2 if no valid moves are available.
    """
    if transposition_table is None:
        transposition_table = {}

    best_score = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    center_cols = [3, 2, 4, 1, 5, 0, 6]
    ordered_moves = [col for col in center_cols if grid[0][col] == ' ']

    for col in ordered_moves:
        row_insert = find_empty_row(grid, col)
        grid[row_insert][col] = player  # Make the move

        position_key = tuple(map(tuple, grid))  # Generate a unique key for the current grid state

        if position_key in transposition_table:
            score = transposition_table[position_key]
        else:
            position = Position(grid, 'R' if player == 'J' else 'J')
            score = -negamax(position, -beta, -alpha, depth=8, transposition_table=transposition_table)
            transposition_table[position_key] = score  # Store the score

        grid[row_insert][col] = ' '  # Undo the move

        if score > best_score:
            best_score = score
            best_move = col

        alpha = max(alpha, score)

        if alpha >= beta:
            break

    return best_move
