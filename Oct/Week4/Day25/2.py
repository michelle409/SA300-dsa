# Problem: Online Stock Span
# Pattern: Monotonic stack - accumulate span of consecutive smaller prices
# Time: O(1) amortized | Space: O(n)

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while len(self.stack) > 0 and self.stack[len(self.stack)-1][0] <= price:
            span = span + self.stack.pop()[1]
        self.stack.append([price, span])
        return span

obj = StockSpanner()
print(obj.next(100))  # 1
print(obj.next(80))   # 1
print(obj.next(60))   # 1
print(obj.next(70))   # 2
print(obj.next(60))   # 1
print(obj.next(75))   # 4
print(obj.next(85))   # 6