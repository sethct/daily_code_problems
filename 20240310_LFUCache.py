#| Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with
#| a cache size n, and contain the following methods:
#| * set(key, value): sets key to value. If there are already n items in the cache and we are
#| adding a new item, then it should also remove the least frequently used item. If there is
#|  a tie, then the least recently used key should be removed.
#| * get(key): gets the value at key. If no such key exists, return null.

class LFUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = self.next = None

class LFUDoublyLinkedList:
    def __init__(self):
        self.sentinel = LFUNode(None, None)  # Sentinel node to ease operations
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.size = 0

    def append(self, node):
        """Append a node to the end (right before the sentinel)."""
        node.next = self.sentinel
        node.prev = self.sentinel.prev
        self.sentinel.prev.next = node
        self.sentinel.prev = node
        self.size += 1

    def remove(self, node):
        """Remove an existing node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop(self):
        """Pop the first real node (right after the sentinel)."""
        if self.size == 0:
            return None
        node = self.sentinel.next
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}  # Map keys to nodes
        self.freq_to_list = {}  # Map frequencies to doubly linked lists of nodes
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self._increase_freq(node)
        return node.value

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._increase_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                self._remove_least_freq_used()
            node = LFUNode(key, value)
            self.key_to_node[key] = node
            self.freq_to_list.setdefault(1, LFUDoublyLinkedList()).append(node)
            self.min_freq = 1

    def _increase_freq(self, node):
        """Helper function to increase the frequency of a node."""
        old_freq = node.freq
        node.freq += 1
        self.freq_to_list[old_freq].remove(node)
        if old_freq == self.min_freq and not self.freq_to_list[old_freq].size:
            self.min_freq += 1
        self.freq_to_list.setdefault(node.freq, LFUDoublyLinkedList()).append(node)

    def _remove_least_freq_used(self):
        """Helper function to remove the least frequently used element."""
        list_to_remove = self.freq_to_list[self.min_freq]
        node_to_remove = list_to_remove.pop()
        del self.key_to_node[node_to_remove.key]
        if not list_to_remove.size:
            del self.freq_to_list[self.min_freq]
