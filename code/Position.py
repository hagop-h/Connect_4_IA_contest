from UtilsPosition import count_consecutive_vertical, count_consecutive_horizontal, count_consecutive_diagonal_right, count_consecutive_diagonal_left , find_empty_row

# -------------------------------------------------------
# Class Definition: Position Class for handling the game state
# -------------------------------------------------------


class Position:
    """
    Represents the current state of the game.
    """

    def __init__(self, grid, current_player):
        """
        Initializes the position of the grid and the current player.
        Parameters:
        - grid: 2D list representing the game board.
        - current_player: Character representing the current player.
        """
        self.grid = [row[:] for row in grid]
        self.current_player = current_player

    def is_terminal(self):
        """
        Determines if the current game state is terminal (i.e., game over).
        Returns: Boolean indicating if the game has ended.
        """
        return self.check_winner() or all(cell != ' ' for row in self.grid for cell in row)

    def evaluate(self):
        """
        Evaluates the game state from the perspective of the 'R' player.
        Returns: Integer score indicating the state's favorability towards 'R'.
        """
        # Positive score for favorable positions for 'R', negative for 'J'
        winner = self.check_winner()
        if winner == 'R':
            return 1000  # AI ('R') wins
        elif winner == 'J':
            return -1000  # Opponent ('J') wins
        elif self.is_terminal():
            return 0

        score = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 'R':
                    score += self.evaluate_position(row, col)
                elif self.grid[row][col] == 'J':
                    score -= self.evaluate_position(row, col)

        return score

    def evaluate_position(self, row, col):
        """
        Evaluates the favorability of a specific position on the board.
        Parameters:
        - row: Row index of the position.
        - col: Column index of the position.
        Returns: Integer score based on proximity to a winning condition.
        """
        proximity_score = 0
        vertical_score = count_consecutive_vertical(self.grid, 'R', row, col)
        horizontal_score = count_consecutive_horizontal(self.grid, 'R', row, col)
        diagonal_score_right = count_consecutive_diagonal_right(self.grid, 'R', row, col)
        diagonal_score_left = count_consecutive_diagonal_left(self.grid, 'R', row, col)
        # Prioritize higher consecutive counts
        proximity_score += max(diagonal_score_right, diagonal_score_left, vertical_score, horizontal_score) ** 2
        return proximity_score

    def generate_moves(self):
        """
        Generates all possible moves for the current player.
        Returns: List of column indices where the player can place their piece.
        """
        return [col for col in range(len(self.grid[0])) if self.grid[0][col] == ' ']

    def play(self, move):
        """
        Plays a move and returns the resulting game state.
        Parameters:
        - move: Column index where the piece is to be placed.
        Returns: New Position object representing the state after the move.
        """
        new_grid = [row[:] for row in self.grid]
        row_insert = find_empty_row(new_grid, move)
        new_grid[row_insert][move] = self.current_player
        return Position(new_grid, 'R' if self.current_player == 'J' else 'J')

    def check_winner(self):
        """
        Checks for a winner in the current game state.
        Returns: Character of the winning player, or None if no winner.
        """
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != ' ':
                    # Check Horizontal
                    if col + 3 < len(self.grid[0]):
                        if (self.grid[row][col] == self.grid[row][col + 1] ==
                                self.grid[row][col + 2] == self.grid[row][col + 3]):
                            return self.grid[row][col]
                    # Check Vertical
                    if row + 3 < len(self.grid):
                        if (self.grid[row][col] == self.grid[row + 1][col] ==
                                self.grid[row + 2][col] == self.grid[row + 3][col]):
                            return self.grid[row][col]
                    # Check Diagonal /
                    if col + 3 < len(self.grid[0]) and row + 3 < len(self.grid):
                        if (self.grid[row][col] == self.grid[row + 1][col + 1] ==
                                self.grid[row + 2][col + 2] == self.grid[row + 3][col + 3]):
                            return self.grid[row][col]
                    # Check Diagonal \
                    if col - 3 >= 0 and row + 3 < len(self.grid):
                        if (self.grid[row][col] == self.grid[row + 1][col - 1] ==
                                self.grid[row + 2][col - 2] == self.grid[row + 3][col - 3]):
                            return self.grid[row][col]
        return None
