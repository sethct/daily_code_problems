#| Given the root to a binary search tree, find the second largest node in the tree.

#-----------------#
# Define Function #
#-----------------#

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findLargest(root):
    current = root
    while current.right is not None:
        current = current.right
    return current

def findSecondLargest(root):
    if root is None or (root.left is None and root.right is None):
        # Tree is empty or has only one node, hence no second largest element
        return None

    current = root
    while current:
        # Case 1: If current node has a right child, but the right child has
        # no children, then current node is the second largest node.
        if current.right is not None and current.right.left is None and current.right.right is None:
            return current

        # Case 2: If current node has no right child, then the second largest
        # node is the largest node in current node's left subtree.
        if current.right is None:
            return findLargest(current.left)

        # Move to the right child if none of the above conditions are met.
        current = current.right

#------------------#
# Test Application #
#------------------#

if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(25)
    root.right.right = TreeNode(35)

    second_largest = findSecondLargest(root)
    if second_largest:
        print(f"The second largest element is {second_largest.val}")
    else:
        print("The tree does not have a second largest element.")
