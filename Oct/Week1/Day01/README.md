# Day 01 — Two Sum
**Topic:** Hashmap lookup

## Primary: Two Sum
**Approach:** One-pass hashmap. Walk through the array, for each number
calculate the complement (target - current). Check if complement is
already in the dict. If yes, return both indices. If no, store current
number and its index in the dict.

**Time:** O(n) | **Space:** O(n)

**Edge case I missed:** nums = [3, 5] target = 6. Complement of 3 is 3, so if I checked after writing to the dict, it would pair index 0 with itself. The fix is checking before writing, that way the current number isn't in the dict yet when I look for its complement.


## Variants

### Two Sum II - Input Array Is Sorted (Two Pointers)
Two pointers, one at the start one at the end. If sum is too small, move left pointer right. If sum is too big, move right pointer left.
Works because the array is sorted. O(n) time, O(1) space.