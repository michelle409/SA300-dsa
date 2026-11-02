# Day 1 - Fibonacci Number
**Topic:** Recursion — base case + recursive step + memoization

## Primary: Fibonacci Number
**Approach:** Recursive helper inside main function. Two base cases:
n=0 returns 0, n=1 returns 1. Before recursing check memo dict —
if answer already computed return it immediately. Otherwise compute
helper(n-1) + helper(n-2), store in memo, return it.

**Time:** O(n) with memo | **Space:** O(n) memo + O(n) call stack

**Edge case I caught:** Without memo fib(50) takes forever — exponential
time because same subproblems computed millions of times. Memo makes
it O(n) by storing each result once.

## Variants

### N-th Tribonacci (Sum of 3 previous instead of 2)
Same memoized recursion pattern. Three base cases: n=0 returns 0,
n=1 and n=2 return 1. Recursive step sums three previous values.

### Climbing Stairs (Same as Fibonacci — different story)
n stairs, can climb 1 or 2 steps. Ways to reach stair n =
ways from stair n-1 + ways from stair n-2. Identical to Fibonacci.
Base case: n<=0 and n=1 both return 1 (one way to stand at bottom).

### Min Cost Climbing Stairs (Pick cheaper entry point)
Cost array — each stair has a cost. Recursion picks minimum of
one step or two steps forward. Start from either index 0 or 1
(can start from either). Return min of helper(0) and helper(1).

### Fibonacci Bottom-Up (Iterative — no recursion no stack overflow)
Build from base cases upward. Only need prev1 and prev2 at any
point — O(1) space. Avoids call stack overflow on very large n.