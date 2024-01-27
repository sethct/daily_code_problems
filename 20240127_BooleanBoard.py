#| You are given an M by N matrix consisting of booleans that represents a board.
#| Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
#| Given this matrix, a start coordinate, and an end coordinate,
#| return the minimum number of steps required to reach the end coordinate from the start.
#| If there is no possible path, then return null. You can move up, left, down, and right.
#| You cannot move through walls. You cannot wrap around the edges of the board.

from collections import deque

#-----------------#
# Define Function #
#-----------------#

def is_valid_move(matrix, x, y, visited):
    #| Check if the next move is within the matrix boundaries,
    #| not a wall, and not already visited.
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and not matrix[x][y] and not visited[x][y]

def min_steps(matrix, start, end):
    #| Handle edge case where the matrix is empty.
    if not matrix or not matrix[0]:
        return None

    #| Initialise rows and columns.
    rows, cols = len(matrix), len(matrix[0])

    #| Create a matrix to keep track of visited cells.
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    #| Define the possible movements (right, down, left, up).
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    
    #| Initialise the queue for Breadth First Search and add the start position.
    #| Each element in the queue is a tuple (x, y, steps).
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    while queue:
        #| Pop the first element in the queue.
        x, y, steps = queue.popleft()

        #| Check if the current position is the end position.
        if (x, y) == end:
            return steps  # Return the number of steps taken.

        #| Explore all possible movements from the current position.
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            #| Check if the move is valid (within boundaries, not a wall, not visited).
            if is_valid_move(matrix, new_x, new_y, visited):
                #| Mark the new position as visited.
                visited[new_x][new_y] = True
                #| Add the new position to the queue with incremented step count.
                queue.append((new_x, new_y, steps + 1))

    #| Return None if there is no path from start to end.
    return None

#------------------#
# Test Application #
#------------------#

matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
start = (3, 0)
end = (0, 0)

print(min_steps(matrix, start, end))
