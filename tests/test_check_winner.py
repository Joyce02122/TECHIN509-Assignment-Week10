import unittest
from models.board import Board  # Import the Board class from models

class TestBoard(unittest.TestCase):

    def test_check_winner(self):
        # Test when there is a winner in a row
        board = Board()
        board.update_board(0, 0, "X")
        board.update_board(0, 1, "X")
        board.update_board(0, 2, "X")
        self.assertEqual(board.check_winner(), "X")  # X wins

        # Test when there is a winner in a column
        board = Board()
        board.update_board(0, 0, "O")
        board.update_board(1, 0, "O")
        board.update_board(2, 0, "O")
        self.assertEqual(board.check_winner(), "O")  # O wins

        # Test when there is a winner in a diagonal
        board = Board()
        board.update_board(0, 0, "X")
        board.update_board(1, 1, "X")
        board.update_board(2, 2, "X")
        self.assertEqual(board.check_winner(), "X")  # X wins in diagonal

        # Test when there is no winner (board is not full)
        board = Board()
        board.update_board(0, 0, "O")
        board.update_board(0, 1, "X")
        self.assertEqual(board.check_winner(), "")  # No winner yet

        # Test when there is no winner (board is full but no winner)
        board = Board()
        board.update_board(0, 0, "O")
        board.update_board(0, 1, "X")
        board.update_board(0, 2, "O")
        board.update_board(1, 0, "X")
        board.update_board(1, 1, "O")
        board.update_board(1, 2, "X")
        board.update_board(2, 0, "O")
        board.update_board(2, 1, "X")
        board.update_board(2, 2, "O")
        self.assertEqual(board.check_winner(), "O")  # O wins in the last column

if __name__ == '__main__':
    unittest.main()
