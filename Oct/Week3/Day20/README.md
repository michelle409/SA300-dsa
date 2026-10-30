# Day 20 - Find Pivot Index
**Topic:** Prefix sum split point

## Primary: Find Pivot Index
**Approach:** Calculate total sum first. Walk through array maintaining
left_sum. At each position right_sum = total - left_sum - nums[i].
If left equals right that index is the pivot. Update left_sum after
the check not before.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Update left_sum AFTER checking. If you add
nums[i] to left_sum first it would include the current element which
should not be in either side.

## Variants

### Find the Middle Index (Identical to primary - different name)
Exact same logic. LeetCode listed it as a separate problem but the
solution is identical.

### Equilibrium Point GFG (Same logic 1-indexed)
Same pivot logic but return i+1 because GFG uses 1-based indexing.

### Minimum Value to Get Positive Step by Step Sum (Track min prefix)
Find the most negative prefix sum reaches. Start value must be high
enough so that even the worst prefix stays positive. Answer is 1 minus
the minimum prefix sum.

### Left and Right Sum Differences (See Day 4)
Already covered.

### Running Sum (See Day 4)
Already covered.