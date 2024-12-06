class Board:
    def __init__(self):
        # Initialize a 3x3 game board with all cells set to empty space " "
        self.grid = [[" " for _ in range(3)] for _ in range(3)] 

    def draw_board(self):
        """
        Draw the Tic-Tac-Toe game board.
        It will print the 3x3 grid of the game with "X", "O", or " ".
        """
        print("-----")
        for row in self.grid:
            print("|", end=" ")
            print(" | ".join(row), end=" ")
            print("|")
            print("-----")
    
    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on the location selected by the player.

        Args:
            row (int): row index of the board
            col (int): column index of the board
            symbol (str): symbol used by the player ('X' or 'O')
        
        Returns:
            bool: True if the move was successful, False if the position is already taken.
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board.

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string.
        """

        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        # If no winner
        return ""

    def is_full(self) -> bool:
        """
        Check if the current board is full or not.

        Returns:
            bool: Boolean value indicating whether the board is full.
        """
        return all(cell != " " for row in self.grid for cell in row)
