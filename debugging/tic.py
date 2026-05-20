#!/usr/bin/python3

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Check for winner before next move
        if check_winner(board):
            print("Player " + ("O" if player == "X" else "X") + " wins!")
            break

        # Ask for valid input
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates. Please enter numbers 0, 1, or 2.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

        # Make the move
        board[row][col] = player
        player = "O" if player == "X" else "X"

        # Check for tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    tic_tac_toe()
