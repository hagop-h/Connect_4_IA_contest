# -----
# AI Game Handling: Helper Functions for Evaluating Game State
# -----

def find_empty_row(grid, col):
    """
    Identifies the first empty row in a specified column from the bottom up.
    Parameters:
    - grid: 2D list representing the game board.
    - col: Integer representing the column to check.
    Returns:
    - The index of the first empty row, or -1 if the column is full.
    """
    for row in range(len(grid) - 1, -1, -1):
        if grid[row][col] == ' ':
            return row
    return -1


def count_consecutive_horizontal(grid, player, row, col):
    """
    Counts consecutive pieces horizontally from a specified position.
    Parameters:
    - grid: 2D list representing the game board.
    - player: Character representing the player's pieces to count.
    - row: Integer representing the row of the starting position.
    - col: Integer representing the column of the starting position.
    Returns:
    - The count of consecutive pieces horizontally.
    """
    count = 1
    # Check to the left
    for c in range(col - 1, -1, -1):
        if grid[row][c] == player:
            count += 1
        else:
            break
    # Check to the right
    for c in range(col + 1, len(grid[0])):
        if grid[row][c] == player:
            count += 1
        else:
            break
    return count


def count_consecutive_vertical(grid, player, row, col):
    """
    Counts consecutive pieces vertically from a specified position.
    Parameters:
    - grid: 2D list representing the game board.
    - player: Character representing the player's pieces to count.
    - row: Integer representing the row of the starting position.
    - col: Integer representing the column of the starting position.
    Returns:
    - The count of consecutive pieces vertically.
    """
    count = 1
    # Check upwards
    for r in range(row - 1, -1, -1):
        if grid[r][col] == player:
            count += 1
        else:
            break
    # Check downwards
    for r in range(row + 1, len(grid)):
        if grid[r][col] == player:
            count += 1
        else:
            break
    return count


def count_consecutive_diagonal_right(grid, player, row, col):
    """
    Counts consecutive pieces diagonally to the right (descending diagonal) from a specified position.
    Parameters:
    - grid: 2D list representing the game board.
    - player: Character representing the player's pieces to count.
    - row: Integer representing the row of the starting position.
    - col: Integer representing the column of the starting position.
    Returns:
    - The count of consecutive pieces diagonally to the right.
    """
    count = 1
    # Check upward-right
    r, c = row - 1, col + 1
    while r >= 0 and c < len(grid[0]):
        if grid[r][c] == player:
            count += 1
        else:
            break
        r -= 1
        c += 1
    # Check downward-left
    r, c = row + 1, col - 1
    while r < len(grid) and c >= 0:
        if grid[r][c] == player:
            count += 1
        else:
            break
        r += 1
        c -= 1
    return count


def count_consecutive_diagonal_left(grid, player, row, col):
    """
    Counts consecutive pieces diagonally to the left (ascending diagonal) from a specified position.
    Parameters:
    - grid: 2D list representing the game board.
    - player: Character representing the player's pieces to count.
    - row: Integer representing the row of the starting position.
    - col: Integer representing the column of the starting position.
    Returns:
    - The count of consecutive pieces diagonally to the left.
    """
    count = 1
    # Check upward-left
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if grid[r][c] == player:
            count += 1
        else:
            break
        r -= 1
        c -= 1
    # Check downward-right
    r, c = row + 1, col + 1
    while r < len(grid) and c < len(grid[0]):
        if grid[r][c] == player:
            count += 1
        else:
            break
        r += 1
        c += 1
    return count

# -----
#  Utils for Game Mode : Tie Detection
# -----

def tie(grid):
    """
    Checks if the game has reached a tie state where no valid moves are available.
    Parameters:
    - grid: 2D list representing the game board.
    Returns:
    - Boolean indicating whether the game is a tie (True if tie, False otherwise).
    """
    # Check each cell in the grid; if any cell is empty, the game is not a tie
    for col in range(0, 6):
        for row in range(len(grid) - 1, -1, -1):
            if grid[row][col] == ' ':
                return True
    return False