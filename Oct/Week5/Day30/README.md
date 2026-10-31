# Day 30 - Move Zeroes
**Topic:** Two pointers read-write revisit

## Primary: Move Zeroes
**Approach:** Write pointer only moves when current element is non-zero.
Copy non-zero elements forward. After loop fill remaining positions
with zeros. In-place O(1) space.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Fill with zeros AFTER the write loop not during.
If you write zeros during the loop you might overwrite elements you
haven't read yet.

## Variants

### Remove Element, Remove Duplicates, Sort By Parity
All covered in Day 10. Same read-write pointer pattern.

### Partition Array According to Given Pivot (Three buckets)
Collect less-than, equal, greater-than pivot into three lists.
Concatenate in order. Stable relative ordering preserved.

### Rotate Array (Three reversals)
Reverse entire array. Reverse first k elements. Reverse rest.
Three reversals achieve rotation in O(1) space. k%n handles
k larger than array length.