from models.board import Board

def play_game():
    # 建立棋盤
    board = Board()
    
    # 定義遊戲步驟 (行, 列, 玩家標誌)
    moves = [
        (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),  # X 和 O 交替下棋
        (1, 0, "O"), (1, 1, "X"), (1, 2, "O"),
        (2, 0, "X"), (2, 1, "O"), (2, 2, "X"),
    ]
    
    # 記錄每一步驟
    for i, (row, col, symbol) in enumerate(moves):
        board.update_board(row, col, symbol)
        print(f"Move {i+1}: Player {symbol} placed on ({row}, {col})")
        board.draw_board()  # 顯示棋盤
        winner = board.check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
    else:
        print("No winner, it's a draw!")

if __name__ == "__main__":
    play_game()
