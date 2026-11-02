# Problem: Min Cost Climbing Stairs
# Pattern: Recursion with memoization - pick cheaper step
# Time: O(n) | Space: O(n)
# DON'T use lru_cache - build memo dict yourself

def minCostClimbingStairs(cost):
    n = len(cost)
    memo = {}

    def helper(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
        return memo[i]

    return min(helper(0), helper(1))

print(minCostClimbingStairs([10, 15, 20]))       # 15
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6