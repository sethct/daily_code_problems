#| Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
#| data structure with the following methods: enqueue, which inserts an element into the queue,
#| and dequeue, which removes it.

#------------------#
# Define Functions #
#------------------#

class MyQueue:
    def __init__(self):
        #| Initialise data structure
        self.enqueueStack = []  # Stack to handle enqueue operations
        self.dequeueStack = []  # Stack to handle dequeue operations

    def enqueue(self, x):
        #| Push the element onto the enqueue stack
        self.enqueueStack.append(x)

    def dequeue(self):
        #| If the dequeue stack is empty, move all elements from the enqueue stack
        if not self.dequeueStack:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        
        #| Pop the top element from the dequeue stack, which is the front element of the queue
        return self.dequeueStack.pop() if self.dequeueStack else None

    def peek(self):
        #| If the dequeue stack is empty, move all elements from enqueue to dequeue stack
        if not self.dequeueStack:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        
        #| Return the top element of the dequeue stack without removing it, if it exists
        return self.dequeueStack[-1] if self.dequeueStack else None

    def empty(self):
    #|The queue is empty only if both stacks are empty
        return not self.enqueueStack and not self.dequeueStack
