# main.py - Deadpool
from functions import print_board, check_winner, make_move, is_full
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Please enter valid numbers between 0 and 2.")
            continue
        if 0 <= row <= 2 and 0 <= col <= 2:
            if make_move(board, current_player, row, col):
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f":tada: Player {winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid input, please choose numbers 0–2.")
if __name__ == "__main__":
    main()