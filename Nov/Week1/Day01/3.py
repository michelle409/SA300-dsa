# Problem: Climbing Stairs
# Pattern: Recursion with memoization - same structure as Fibonacci
# Time: O(n) | Space: O(n)
# DON'T use lru_cache - build memo dict yourself

def climbStairs(n):
    memo = {}

    def helper(n):
        if n <= 0:
            return 1
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)

print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
print(climbStairs(5))  # 8