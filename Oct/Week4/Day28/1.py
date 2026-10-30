# Problem: Number of Recent Calls
# Pattern: Queue - sliding time window
# Time: O(1) amortized | Space: O(n)
# DON'T use collections.deque - use plain list

class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)

obj = RecentCounter()
print(obj.ping(1))     # 1
print(obj.ping(100))   # 2
print(obj.ping(3001))  # 3
print(obj.ping(3002))  # 3