# Problem: Fibonacci Bottom-Up
# Pattern: Iterative DP - build from base cases upward
# Time: O(n) | Space: O(1)
# DON'T use recursion here - point is to show iterative approach

def fibBottomUp(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1

print(fibBottomUp(0))   # 0
print(fibBottomUp(1))   # 1
print(fibBottomUp(5))   # 5
print(fibBottomUp(10))  # 55