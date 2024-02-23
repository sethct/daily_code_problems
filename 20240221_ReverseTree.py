#| Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
#| For example, given the following preorder traversal:
#| [a, b, d, e, c, f, g]
#| And the following inorder traversal:
#| [d, b, e, a, f, c, g]

#------------------#
# Define Functions #
#------------------#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # The first element in preorder list is the root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder list
    mid_idx = inorder.index(root_val)

    # Recursively construct the left and right subtree
    root.left = buildTree(preorder[1:mid_idx+1], inorder[:mid_idx])
    root.right = buildTree(preorder[mid_idx+1:], inorder[mid_idx+1:])

    return root

# Helper function to print inorder traversal of the tree for verification
def printInorder(node):
    if node:
        # First recur on left child
        printInorder(node.left)
        # Then print the data of node
        print(node.val, end=' ')
        # Now recur on right child
        printInorder(node.right)

# Given preorder and inorder traversals
preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

# Reconstruct the binary tree
root = buildTree(preorder, inorder)

# Print inorder traversal of the constructed tree for verification
printInorder(root)
