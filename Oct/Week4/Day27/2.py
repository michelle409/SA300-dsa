# Problem: Implement Stack using Queues
# Pattern: One queue - rotate on push to maintain LIFO
# Time: O(n) push, O(1) pop | Space: O(n)

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0