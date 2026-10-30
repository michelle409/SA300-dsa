# Problem: Moving Average from Data Stream
# Pattern: Queue simulation - fixed window running sum
# Time: O(1) | Space: O(size)

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.window_sum = 0

    def next(self, val):
        if len(self.queue) == self.size:
            self.window_sum = self.window_sum - self.queue.pop(0)
        self.queue.append(val)
        self.window_sum = self.window_sum + val
        return self.window_sum / len(self.queue)

obj = MovingAverage(3)
print(obj.next(1))   # 1.0
print(obj.next(10))  # 5.5
print(obj.next(3))   # 4.67
print(obj.next(5))   # 6.0