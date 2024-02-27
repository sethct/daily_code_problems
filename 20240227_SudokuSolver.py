#| Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
#| The objective is to fill the grid with the constraint that every row, column, and
#| box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
#| Implement an efficient sudoku solver.

#------------------#
# Define Functions #
#------------------#

def is_valid(board, row, col, num):
    #| Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    #| Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    #| Check 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Reset the cell for backtracking

    return False  # Triggers backtracking

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

#------------------#
# Test Application #
#------------------#
        
if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_board):
        print_board(sudoku_board)
    else:
        print("No solution exists.")
