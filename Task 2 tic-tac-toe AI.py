import math

def print_board(board, step):
    if step == 1:
        for i in range(0, 9, 3):
            row = " | ".join(str(x) if x != ' ' else str(i + j + 1) for j, x in enumerate(board[i:i + 3]))
            print(row)
            if i < 6:
                print("-" * 9)
    else:
        for i in range(0, 9, 3):
            row = " | ".join(board[i:i + 3])
            print(row)
            if i < 6:
                print("-" * 5)

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return -1 if maximizing_player else 1

    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '

            if move_val > best_val:
                best_move = i
                best_val = move_val

    return best_move

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    step = 1

    while True:
        print("\nCurrent board:")
        print_board(board, step)

        try:
            user_move = int(input("Enter your move (1-9): ")) - 1
            if board[user_move] != ' ' or not (0 <= user_move <= 8):
                raise ValueError
        except (ValueError, IndexError):
            print("Invalid move try again.")
            continue

        board[user_move] = 'X'
        step += 1

        if check_winner(board):
            print_board(board, step)
            print("You win!")
            break
        elif is_board_full(board):
            print_board(board, step)
            print("It's a tie!")
            break

        print("\nai move:")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'
        step += 1

        if check_winner(board):
            print_board(board, step)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board, step)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
