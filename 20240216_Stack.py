#| Implement a stack that has the following methods:
#| push(val), which pushes an element onto the stack
#| pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
#| max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
#| Each method should run in constant time.

#-----------------#
# Define Function #
#-----------------#

class MaxStack:
    def __init__(self):
        # Main stack to store all the elements
        self.main_stack = []
        # Auxiliary stack to store the maximums
        self.max_stack = []

    def push(self, val):
        self.main_stack.append(val)
        #| If the max stack is empty or the current value is greater than the current maximum,
        #| push the value onto the max stack
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if not self.main_stack:
            #| Throw an error if the stack is empty
            raise IndexError("pop from an empty stack")
        val = self.main_stack.pop()
        #| If the popped value is the same as the top of the max stack, pop it from the max stack too
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def max(self):
        if not self.max_stack:
            #| Throw an error if the stack is empty
            raise ValueError("max from an empty stack")
        return self.max_stack[-1]

# Example usage
if __name__ == "__main__":
    stack = MaxStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    print(stack.max())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.max())  # Output: 3
    stack.push(5)
    print(stack.max())  # Output: 5
