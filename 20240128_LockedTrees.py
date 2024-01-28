#| Implement locking in a binary tree.
#| A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
#| Design a binary tree node class with the following methods:
#| is_locked, which returns whether the node is locked
#| lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
#| unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
#| You may augment the node to add parent pointers or any other property you would like.
#| You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
#| Each method should run in O(h), where h is the height of the tree.

class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        #| Initialise the node with the given value and optional left, right children, and parent.
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.is_locked = False  # Initially, the node is not locked.
        self.locked_descendants_count = 0  # Count of locked descendants.

        #| Set this node as the parent of its children, if they exist.
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def can_lock_or_unlock(self):
        #| This method checks whether the node can be locked or unlocked.
        #| A node can be locked or unlocked only if none of its ancestors are locked.

        #| Check if any ancestors are locked
        current = self.parent
        while current:
            if current.is_locked:
                return False  # An ancestor is locked, so this node cannot be locked/unlocked.
            current = current.parent

        #| If no ancestors are locked, check if any descendants are locked
        return self.locked_descendants_count == 0

    def lock(self):
        #| Attempt to lock the node.
        #| If the node is already locked or if it cannot be locked (due to locked ancestors or descendants),
        #| return False.
        if self.is_locked or not self.can_lock_or_unlock():
            return False

        #| Lock this node and update the locked descendants count of all ancestors.
        self.is_locked = True
        current = self.parent
        while current:
            current.locked_descendants_count += 1
            current = current.parent

        return True

    def unlock(self):
        #| Attempt to unlock the node.
        #| If the node is not locked or if it cannot be unlocked (due to locked ancestors or descendants),
        #| return False.
        if not self.is_locked or not self.can_lock_or_unlock():
            return False

        #| Unlock this node and update the locked descendants count of all ancestors.
        self.is_locked = False
        current = self.parent
        while current:
            current.locked_descendants_count -= 1
            current = current.parent

        return True

    def is_locked(self):
        #| Return whether the node is currently locked.
        return self.is_locked
