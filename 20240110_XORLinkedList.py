#| Implement an XOR linked list; it has an add(element) which adds the element to the end,
#| and a get(index) which returns the node at index.


import ctypes

class Node:
    def __init__(self, data):
        # Node constructor, initializes a new node with the given data
        self.data = data
        self.both = None  # XOR of next and prev nodes

class XORLinkedList:
    def __init__(self):
        # XORLinkedList constructor, initializes an empty list with no head or tail
        self.head = None
        self.tail = None

    def add(self, data):
        # Add a new node with the given data to the end of the XOR linked list
        new_node = Node(data)

        if not self.head:
            # If the list is empty, the new node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Calculate XOR of current tail's both and None (next node)
            new_node.both = self.get_pointer(self.tail) ^ 0

            # Update the current tail's both to XOR with the new node
            self.tail.both = self.tail.both ^ self.get_pointer(new_node)

            # Update the tail to the new node
            self.tail = new_node

    def get(self, index):
        # Retrieve the node at the specified index in the XOR linked list
        current = self.head
        prev_address = 0

        for i in range(index):
            # Calculate the next node's address by XORing the current node's both and the previous node's address
            next_address = prev_address ^ self.get_pointer(current.both)

            if next_address:
                # If there is a next node, move to the next node
                prev_address = self.get_pointer(current)
                current = self.dereference_pointer(next_address)
            else:
                # If index is out of bounds, return None
                return None

        return current

    def get_pointer(self, node):
        # Get the memory address of a node
        return id(node)

    def dereference_pointer(self, address):
        # Convert a memory address back to a node
        return ctypes.cast(address, ctypes.py_object).value

# Example usage:
xor_list = XORLinkedList()
xor_list.add(1)
xor_list.add(2)
xor_list.add(3)

# Retrieve node at index 1
node_at_index_1 = xor_list.get(1)
if node_at_index_1:
    print("Node at index 1:", node_at_index_1.data)
else:
    print("Index out of bounds.")
