# Problem: N-th Tribonacci Number
# Pattern: Recursion with memoization - same as fib but sum of 3 previous
# Time: O(n) | Space: O(n)
# DON'T use lru_cache - build memo dict yourself

def tribonacci(n):
    memo = {}

    def helper(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
        return memo[n]

    return helper(n)

print(tribonacci(4))   # 4
print(tribonacci(25))  # 1389537