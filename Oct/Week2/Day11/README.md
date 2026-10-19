# Day 11 - Merge Sorted Array
**Topic:** Two pointers from the end (in-place merge)

## Primary: Merge Sorted Array
**Approach:** Three pointers - p1 at end of nums1 valid elements, p2 at
end of nums2, p at the very end of nums1. Compare from the back and
place the larger element at position p. Move inward. If nums2 has
remaining elements copy them over. Merging from the back avoids
overwriting unprocessed elements.

**Time:** O(m+n) | **Space:** O(1)

**Edge case I caught:** When nums1 elements are all smaller than nums2,
p1 reaches -1 first. The second while loop copies remaining nums2
elements to the front of nums1.

## Variants

### Merge Two Sorted Lists (Linked list merge with dummy node)
Use a dummy node as the head of the merged list. Compare values at
both list heads, attach the smaller one to current, advance that
pointer. When one list runs out attach the rest of the other.

### Merge Intervals (Sort by start + merge overlapping)
Sort intervals by start time using bubble sort. Walk through and if
current interval overlaps with last result interval merge them by
updating the end. Otherwise add as new interval.

### Insert Interval (Three phase - before, overlap, after)
Phase 1 add all intervals ending before new interval starts. Phase 2
merge all intervals overlapping with new interval. Phase 3 add
remaining intervals. O(n) time no sort needed.

### Decompress Run-Length Encoded List (Walk pairs, repeat value)
Walk through array in steps of 2. Each pair is freq and val. Repeat
val freq times and append to result. range(0, len, 2) steps by 2.