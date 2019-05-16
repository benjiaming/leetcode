"""
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""
#%%

class MinStack():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.min_stack) and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack == []:
            return None
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)

minStack.push(-3)
minStack.push(3)
print(minStack.stack) # [-2,0,-3,3]
print(minStack.top())
print(minStack.getMin())

minStack.pop()
print(minStack.stack) # [-2,0,-3]
print(minStack.top())
print(minStack.getMin())

#%%
