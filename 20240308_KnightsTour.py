#| A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
#| Given N, write a function to return the number of knight's tours on an N by N chessboard.

#------------------#
# Define Functions #
#------------------#

def is_valid_move(x, y, board):
    """Check if (x,y) is a valid move."""
    if (0 <= x < len(board)) and (0 <= y < len(board)) and board[x][y] == -1:
        return True
    return False

def knight_tours_util(n, board, x, y, move_x, move_y, pos=1):
    """Util function to perform the knight's tour using backtracking."""
    if pos == n**2:
        return 1  # A complete tour has been found
    
    #| Try all next moves from the current coordinate x, y
    num_tours = 0
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = pos
            num_tours += knight_tours_util(n, board, next_x, next_y, move_x, move_y, pos+1)
            board[next_x][next_y] = -1  # Backtrack
    return num_tours

def knight_tours(n):
    """Returns the number of knight's tours on an N by N chessboard."""
    board = [[-1 for _ in range(n)] for _ in range(n)]
    #| All possible moves a knight can make
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    board[0][0] = 0  # Start from the first cell
    return knight_tours_util(n, board, 0, 0, move_x, move_y)

#------------------#
# Test Application #
#------------------#

n = 5
print(f"Number of knight's tours on a {n}x{n} chessboard: {knight_tours(n)}")
