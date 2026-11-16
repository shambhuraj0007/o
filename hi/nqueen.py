
# Function to check whether a queen can be placed safely
def is_safe(board, row, col, n):

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower-left diagonal
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Position is safe
    return True


# Function to solve N-Queens using backtracking
def solve_n_queens(board, col, n):

    # If all columns are filled, solution is found
    if col >= n:
        return True

    # Try every row in the current column
    for row in range(n):

        # Check whether the position is safe
        if is_safe(board, row, col, n):

            # Place the queen at the safe position
            board[row][col] = 1

            # Recursively place the next queen
            if solve_n_queens(board, col + 1, n):
                return True

            # Remove the queen if solution fails
            board[row][col] = 0

    # No safe position found in this column
    return False


# Accept the size of chessboard
n = int(input("Enter value of N: "))

# Check minimum board size
if n < 4:
    print("No solution for N less than 4.")

else:
    # Create an N x N chessboard filled with zeros
    board = [[0 for j in range(n)] for i in range(n)]

    # Accept the row of the first queen (1-based)
    first_row = int(input("Enter first queen row (1 to N): "))

    # Convert row number into Python index
    first_row -= 1

    # Place the first queen in the first column
    if first_row < 0 or first_row >= n:
        print("Invalid row position.")

    else:
        board[first_row][0] = 1

        # Start backtracking from the second column
        if solve_n_queens(board, 1, n):

            # Display the final chessboard
            print("N-Queens Solution:")

            # Print each row of the board
            for row in board:

                # Display Q for queen and . for empty position
                print(" ".join("Q" if x == 1 else "." for x in row))

        else:
            # Display message if no solution exists
            print("No solution exists for this first queen position.")
