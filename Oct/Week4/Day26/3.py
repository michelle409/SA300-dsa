# Problem: Daily Temperatures
# Pattern: Monotonic stack - next warmer day
# Time: O(n) | Space: O(n)

def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    for i in range(n):
        while len(stack) > 0 and temperatures[stack[len(stack)-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(dailyTemperatures([30,40,50,60]))               # [1,1,1,0]
print(dailyTemperatures([30,60,90]))                  # [1,1,0]