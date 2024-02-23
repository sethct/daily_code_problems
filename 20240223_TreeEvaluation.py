#| Suppose an arithmetic expression is given as a binary tree. 
#| Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
#| Given the root to such a tree, write a function to evaluate it.
#| For example, given the following tree:
#|
#|    *
#|   / \
#|  +    +
#| / \  / \
#|3  2  4  5

#|You should return 45, as it is (3 + 2) * (4 + 5).

#------------------#
# Define Functions #
#------------------#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateExpression(root):
    if root is None:
        return 0
    #| If it is a leaf node, return its value
    if root.left is None and root.right is None:
        return int(root.val)
    #| Recursively evaluate the left and right subtrees
    left_val = evaluateExpression(root.left)
    right_val = evaluateExpression(root.right)
    #| Apply the operation represented by the current node to the values from the left and right subtrees
    if root.val == '+':
        return left_val + right_val
    elif root.val == '-':
        return left_val - right_val
    elif root.val == '*':
        return left_val * right_val
    elif root.val == '/':
        return left_val / right_val

#| Construct the example tree
root = TreeNode('*')
root.left = TreeNode('+', TreeNode(3), TreeNode(2))
root.right = TreeNode('+', TreeNode(4), TreeNode(5))

#| Evaluate the expression represented by the tree
result = evaluateExpression(root)
print(result)  # Output: 45
