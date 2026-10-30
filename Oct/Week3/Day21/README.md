# Day 21 - Range Sum Query - Immutable
**Topic:** Prefix sum - build once query many in O(1)

## Primary: Range Sum Query - Immutable
**Approach:** Build prefix array once in __init__. prefix[i] stores
sum of all elements from index 0 to i-1. Query any range in O(1)
using prefix[right+1] - prefix[left]. The +1 offset means prefix[0]=0
acts as base case for subarrays starting at index 0.

**Time:** O(n) build, O(1) query | **Space:** O(n)

**Edge case I caught:** prefix has n+1 elements not n. The extra 0 at
the start handles the case where left=0 — subtracting prefix[0]=0
gives the full sum from the start.

## Variants

### Range Sum Query 2D (2D prefix matrix)
Same idea extended to 2D. prefix[i][j] = sum of rectangle from (0,0)
to (i-1,j-1). Query any rectangle using inclusion-exclusion formula.

### Subarray Sum Equals K (See Pattern A)
Running prefix sum plus hashmap. Already covered.

### Continuous Subarray Sum (Prefix mod + hashmap)
Same prefix + hashmap idea but use modulo. If two positions have same
prefix%k the subarray between them is divisible by k. Need length ≥ 2
so gap must be ≥ 2. Seed {0:-1} for subarrays starting at index 0.

### Product of Array Except Self (Prefix product + suffix product)
Two passes. First pass fills result with prefix products. Second pass
multiplies by suffix products from the right. No division needed.
O(n) time O(1) extra space.

### Range Sum Query Mutable (Rebuild prefix on update)
Same prefix array but rebuild from the updated index onwards when a
value changes. O(n) per update but O(1) per query. Optimal uses
segment tree but that's beyond current scope.