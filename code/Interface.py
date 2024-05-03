# -----
#  Interface Functions :  Display grid
# -----

def print_board(grid):
    """
    Prints the game board in a user-friendly format.
    Parameters:
    - grid: 2D list representing the game board where each cell can be empty or filled by a player's marker.
    """
    column_indices = "   ".join(str(i) for i in range(len(grid[0])))
    horizontal_line = "+-" + "-+-".join(["-" for _ in range(len(grid[0]))]) + "-+"

    print(" ", column_indices)
    print(horizontal_line)

    for row in grid:
        print("| " + " | ".join(row) + " |")

    print(horizontal_line)