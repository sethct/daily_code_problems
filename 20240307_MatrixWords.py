#| Given a 2D matrix of characters and a target word,
#| write a function that returns whether the word can
#| be found in the matrix by going left-to-right, or up-to-down.

#------------------#
# Define Functions #
#------------------#

def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)
    
    #| Check if it's possible to have the word in the given direction
    def check_direction(row, col, delta_row, delta_col):
        for i in range(word_length):
            if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != word[i]:
                return False
            row += delta_row
            col += delta_col
        return True
    
    for row in range(rows):
        for col in range(cols):
            #| Check right (left-to-right)
            if check_direction(row, col, 0, 1):
                return True
            #| Check down (up-to-down)
            if check_direction(row, col, 1, 0):
                return True
                
    return False

#------------------#
# Test Application #
#------------------#

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

print(find_word(matrix, 'FOAM'))  # Output: True
print(find_word(matrix, 'MASS'))  # Output: True
