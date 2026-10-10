# Day 04 - Running Sum of 1d Array
**Topic:** Prefix sum intro

## Primary: Running Sum of 1d Array
**Approach:** Walk through the array starting from index 1. For each
position, add the previous element to the current one. This builds
the running sum in place without needing extra space. Start at 1
because index 0 has nothing before it.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Single element array - range(1, 1) is empty
so the loop never runs and the single element is returned as is.

## Variants

### Range Sum Query Immutable (Prefix sum - build once query many)
Build a prefix sum array once in the constructor. To answer any
range query in O(1), return prefix[right+1] - prefix[left]. This
avoids recalculating the sum every time a query is made.

### Shuffle the Array (Index arithmetic - interleave two halves)
First half contains x values, second half contains y values. Walk
from 0 to n, take nums[i] from the first half and nums[i+n] from
the second half, append both to result. O(n) time, O(n) space.

### Richest Customer Wealth (2D array - sum rows, track max)
Nested loops - outer loop goes through each customer, inner loop
sums their bank accounts. Track the maximum wealth seen so far and
update it whenever a higher wealth is found. O(m*n) time, O(1) space.

### Left and Right Sum Differences (Prefix and suffix sum arrays)
Build left sum array going forward and right sum array going
backward. Then for each index take the absolute difference between
left and right sums. Loop backward using range(n-2, -1, -1).
O(n) time, O(n) space.