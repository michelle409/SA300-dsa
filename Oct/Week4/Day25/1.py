# Problem: Min Stack
# Pattern: Augmented stack - second stack tracks minimums
# Time: O(1) all ops | Space: O(n)
# DON'T use heapq - all 4 ops must be O(1)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[len(self.min_stack)-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def getMin(self):
        return self.min_stack[len(self.min_stack)-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # -3
obj.pop()
print(obj.top())     # 0
print(obj.getMin())  # -2