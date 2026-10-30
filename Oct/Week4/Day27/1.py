# Problem: Implement Queue using Stacks
# Pattern: Two stacks - input stack and output stack
# Time: O(1) amortized push/pop | Space: O(n)
# DON'T use collections.deque - that IS a queue already

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        return self.out_stack[len(self.out_stack)-1]

    def empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def _transfer(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())   # 1
print(obj.pop())    # 1
print(obj.empty())  # False