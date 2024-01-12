#| A unival tree is a tree where all nodes under it have the same value.
#| Given the root to a binary tree, count the number of unival subtrees.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

def helper(node):
    #|Base case: an empty tree is a unival tree
    if node is None:
        return 0, True
    
    #| Recursive call for the left subtree
    left_count, is_left_unival = helper(node.left)
    #| Recursive call for the right subtree
    right_count, is_right_unival = helper(node.right)

    #| Check if the current subtree is a unival tree
    if is_left_unival and is_right_unival:
        #| Check if the left child has the same value as the current node
        if (node.left is not None and node.left.value == node.value) or node.left is None:
            #| Check if the right child has the same value as the current node
            if (node.right is not None and node.right.value == node.value) or node.right is None:
                #| Current subtree is a unival tree
                return left_count + right_count + 1, True
            
    #| Current subtree is not a unival tree
    return left_count + right_count, False

#-------------#
# Example Use #
#-------------#

#| Create sample binary tree
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)

#| Count the number of unival subtrees
result = count_unival_subtrees(root)
print('Number of unival subtrees:', result)