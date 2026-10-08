# Day 02 - Contains Duplicate
**Topic:** Set membership

## Primary: Contains Duplicate
**Approach:** Walk through the array, for each number check if it is
already in the set. If yes, return True - duplicate found. If no,
add it to the set and move on. Check before add so we catch the
first duplicate immediately.

**Time:** O(n) | **Space:** O(n)

**Edge case I caught:** Empty array or single element - no duplicates
possible, the loop ends and returns False naturally.

## Variants

### Contains Duplicate II (Hashmap - store last seen index)
Use a dict to store each number and its last seen position. If the
same number appears again and the distance between positions is less
than or equal to k, return True. O(n) time, O(n) space.

### Find All Duplicates in an Array (In-place marking)
Use the array itself as a hashmap. For each number, go to position
abs(nums[i]) - 1 and make it negative to mark as visited. If it is
already negative when you visit, that number is a duplicate. O(n)
time, O(1) space.

### Duplicate Zeros (In-place modification)
Build a temp list by copying each element and adding an extra zero
whenever a zero is found. Then copy the first n elements back into
the original array. O(n) time, O(n) space.