# Problem: Logger Rate Limiter
# Pattern: Hashmap - track last print time per message
# Time: O(1) | Space: O(n)

class Logger:
    def __init__(self):
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.last_printed or timestamp - self.last_printed[message] >= 10:
            self.last_printed[message] = timestamp
            return True
        return False

obj = Logger()
print(obj.shouldPrintMessage(1, "foo"))   # True
print(obj.shouldPrintMessage(2, "bar"))   # True
print(obj.shouldPrintMessage(3, "foo"))   # False
print(obj.shouldPrintMessage(8, "bar"))   # False
print(obj.shouldPrintMessage(10, "foo"))  # False
print(obj.shouldPrintMessage(11, "foo"))  # True