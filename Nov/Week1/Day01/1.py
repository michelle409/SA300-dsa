# Problem: Fibonacci Number
# Pattern: Recursion with memoization - base case + recursive step
# Time: O(n) with memo | Space: O(n) memo dict + O(n) call stack
# DON'T use functools.lru_cache or @cache - write memo dict yourself

def fib(n):
    memo = {}

    def helper(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)

print(fib(0))   # 0
print(fib(1))   # 1
print(fib(2))   # 1
print(fib(5))   # 5
print(fib(10))  # 55