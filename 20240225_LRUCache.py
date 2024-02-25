#------------------#
# Define Functions #
#------------------#

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps keys to their node in the doubly linked list
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail  # Initialize the list as empty
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the accessed node to the most recently used position
            self._add(node)
            return node.value
        return -1

    def set(self, key: int, value: int):
        if key in self.cache:  # Update the value if the key exists
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:  # If over capacity, remove the least recently used item
            # The least recently used item is right after the head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

#------------------#
# Test Applicaiton #
#------------------#

lru_cache = LRUCache(2)
lru_cache.set(1, 1)
lru_cache.set(2, 2)
print(lru_cache.get(1))  # Should return 1
lru_cache.set(3, 3)  # This operation will make key 2 as the least recently used and remove it
print(lru_cache.get(2))  # Should return -1 (not found)
lru_cache.set(4, 4)  # This operation will remove key 1
print(lru_cache.get(1))  # Should return -1 (not found)
print(lru_cache.get(3))  # Should return 3
print(lru_cache.get(4))  # Should return 4
