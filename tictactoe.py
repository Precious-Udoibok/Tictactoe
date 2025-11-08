def play(board):
    x_count = board.count("x")
    o_count = board.count("o")
    if x_count == o_count:
        turn = "x"
        opponent = "o"
    else:
        turn = "o"
        opponent = "x"

    winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    #  Check if we can win this turn
    for combo in winning_combos:
        values = [board[i] for i in combo]
        if values.count(turn) == 2 and values.count("") == 1:
            return combo[values.index("")]

    # Check if opponent can win next and  block them
    for combo in winning_combos:
        values = [board[i] for i in combo]
        if values.count(opponent) == 2 and values.count("") == 1:
            return combo[values.index("")]

    if board[4] == "":
        return 4

    # pick any empty corner
    for i in [0, 2, 6, 8]:
        if board[i] == "":
            return i

    # just pick any empty space
    for i in range(9):
        if board[i] == "":
            return i


def print_board(board):
    """Display the board nicely."""
    symbols = [cell.upper() if cell else " " for cell in board]
    print(f"""
     {symbols[0]} | {symbols[1]} | {symbols[2]}
    ---+---+---
     {symbols[3]} | {symbols[4]} | {symbols[5]}
    ---+---+---
     {symbols[6]} | {symbols[7]} | {symbols[8]}
    """)


def check_winner(board):
    """Check if there's a winner."""
    winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combo in winning_combos:
        values = [board[i] for i in combo]
        if values[0] != "" and values.count(values[0]) == 3:
            return values[0]
    return None


def main():
    board = [""] * 9
    print("Welcome to Tic Tac Toe!")
    print("You are X. AI is O.")
    print_board(board)

    while True:
        # Player move
        try:
            move = int(input("Enter your move (0–8): "))
            if move < 0 or move > 8 or board[move] != "":
                print(" Invalid move, try again.")
                continue
            board[move] = "x"
        except ValueError:
            print(" Please enter a number between 0 and 8.")
            continue

        print_board(board)

        # Check if player won
        winner = check_winner(board)
        if winner == "x":
            print("You win!")
            break
        if "" not in board:
            print(" It's a draw!")
            break

        # AI move
        ai_move = play(board)
        board[ai_move] = "o"
        print(f"AI plays at position {ai_move}:")
        print_board(board)

        # Check if AI won
        winner = check_winner(board)
        if winner == "o":
            print(" AI wins!")
            break
        if "" not in board:
            print(" It's a draw!")
            break


if __name__ == "__main__":
    main()
