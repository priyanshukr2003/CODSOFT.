# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (
            (board[i] == board[i + 3] == board[i + 6] == player) or
            (board[3 * i] == board[3 * i + 1] == board[3 * i + 2] == player)
        ):
            return True

    if (
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    ):
        return True

    return False
def minimax(board, depth, is_maximizing):
    # Base cases: check if the game is over or depth limit reached
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
def ai_move(board):
    best_move = -1
    best_score = -float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move
while True:
    display_board(board)

    # Human player's turn
    move = int(input("Enter your move (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move. Try again.")
        continue

    # Check if human player wins
    if check_win(board, "X"):
        display_board(board)
        print("You win!")
        break

    # Check for a draw
    if " " not in board:
        display_board(board)
        print("It's a draw!")
        break

    # AI player's turn
    ai_best_move = ai_move(board)
    board[ai_best_move] = "O"

    # Check if AI player wins
    if check_win(board, "O"):
        display_board(board)
        print("AI wins!")
        break