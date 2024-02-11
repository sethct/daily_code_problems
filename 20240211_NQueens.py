#| You have an N by N board. Write a function that, given N,
#| returns the number of possible arrangements of the board
#| where N queens can be placed on the board without threatening
#| each other, i.e. no two queens share the same row, column, or diagonal.

#-----------------#
# Define Function #
#-----------------#

def totalNQueens(N):
    #| Board represented by an array where index represents row and value represents column
    #| where the queen is placed in that row.
    board = [-1] * N
    
    #| Counter for valid arrangements
    count = [0]

    def isSafe(row, col):
        for previousRow in range(row):
            #| Get the column of the previously placed queen
            previousCol = board[previousRow]
            
            #| Check if they're in the same column or on the same diagonal.
            #| Diagonals are checked by the equality |currentRow - previousRow| == |currentCol - previousCol|
            if previousCol == col or abs(previousCol - col) == abs(previousRow - row):
                return False
        return True

    def solve(row):
        #| If N queens are placed successfully, increment the count
        if row == N:
            count[0] += 1
            return
        
        #| Try placing a queen in each column of the current row and check if it's safe
        for col in range(N):
            if isSafe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    #| Start solving from the first row
    solve(0)

    return count[0]

#------------------#
# Test Application #
#------------------#

N = 4
print(f"Total solutions for a {N}x{N} board: {totalNQueens(N)}")
