# Problem: Design Hit Counter
# Pattern: Queue - count hits in last 300 seconds
# Time: O(n) | Space: O(n)

class HitCounter:
    def __init__(self):
        self.queue = []

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while len(self.queue) > 0 and self.queue[0] <= timestamp - 300:
            self.queue.pop(0)
        return len(self.queue)

obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))    # 3
obj.hit(300)
print(obj.getHits(300))  # 4
print(obj.getHits(301))  # 3