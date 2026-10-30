# Day 26 - Next Greater Element I
**Topic:** Monotonic decreasing stack

## Primary: Next Greater Element I
**Approach:** Walk through nums2 maintaining a monotonic decreasing
stack. When current element is greater than stack top, the top has
found its next greater element. Pop and record in hashmap. Push current.
Remaining stack elements have no next greater - set to -1. Query
hashmap for each nums1 element.

**Time:** O(n+m) | **Space:** O(n)

**Edge case I caught:** Elements remaining in stack after full pass
have no next greater element - must explicitly set them to -1.

## Variants

### Next Greater Element II (Circular - double the array)
Same monotonic stack but iterate 2*n times using i%n to simulate
circular wrap. Only push indices during first n iterations.

### Daily Temperatures (Next warmer day - store indices)
Same pattern but store indices not values. When popping, distance
between current index and popped index is the days to wait.

### Largest Rectangle in Histogram (Monotonic increasing stack)
Reversed direction - monotonic INCREASING stack. Append sentinel 0
at end. When stack top is taller than current bar, pop and calculate
max rectangle using current index minus new top minus 1 as width.