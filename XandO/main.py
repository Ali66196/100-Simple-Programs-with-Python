# بازی Tic Tac Toe

# تابعی برای چاپ صفحه بازی
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# تابعی برای بررسی برنده
def check_winner(board):
    # بررسی سطرها، ستون‌ها و قطرها برای برنده
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

# تابع بازی Tic Tac Toe
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # ساخت صفحه بازی خالی
    current_player = "X"  # شروع با X

    for turn in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell is already taken! Try again.")
            continue
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        current_player = "O" if current_player == "X" else "X"  # تغییر نوبت بین X و O
    else:
        print_board(board)
        print("It's a tie!")

# فراخوانی تابع بازی
tic_tac_toe()
