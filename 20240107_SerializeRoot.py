#| Given the root to a binary tree, implement serialize(root),
#| which serializes the tree into a string, and deserialize(s),
#| which deserializes the string back into the tree.

#------------------#
# Define Functions #
#------------------#

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialise(root):
    #| serialise the tree using a preorder traversal
    if not root:
        #| If the node is None, assign value of 'None'
        return 'None,'
    #| Represent the node value as a string and serialise its left and right subtrees
    return str(root.val) + ',' + serialise(root.left) + serialise(root.right)

def deserialise(data):
    #| Split the serialised string into a list of nodes
    nodes = data.split(',')
    #| call the helper function to recursively build the tree
    return deserialise_helper(nodes)

def deserialise_helper(nodes):
    #| Add the first element from the list
    if nodes[0] == 'None':
        #| If the leemt is 'None', return None to represent a null node
        nodes.pop(0)
        return None
    #| Creat a TreeNode witha  value of the first Element
    root = TreeNode(int(nodes[0]))
    #| Remove the processed element
    nodes.pop(0)
    #| Recursively build the left and right subtrees
    root.left = deserialise_helper(nodes)
    root.right = deserialise_helper(nodes)

    #| Return the constructed root of the subtree
    return root

#-------------#
# Application #
#-------------#

#| Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

#| Serialise the tree
serialised_tree = serialise(root)
print('Serialised Tree:', serialised_tree)

#| Deserialise the string back to a tree
deserialised_tree = deserialise(serialised_tree)