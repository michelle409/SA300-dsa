# Day 12 - Squares of a Sorted Array
**Topic:** Two pointers from both ends (compare absolute values)

## Primary: Squares of a Sorted Array
**Approach:** Biggest square is always at one of the two ends since the
array is sorted. Use three pointers - left at start, right at end, pos
at end of result. Compare squares of left and right, place the bigger
one at pos and move that pointer inward. Fill result from back to front.

**Time:** O(n) | **Space:** O(n)

**Edge case I caught:** When left equals right both pointers are on the
same element. Use left <= right not left < right so the last element
gets processed.

## Variants

### Sort Array By Parity II (Two pointers - even index even number)
Walk through nums. Even numbers go to even indices, odd numbers go to
odd indices. Keep two separate write pointers - even starts at 0 steps
by 2, odd starts at 1 steps by 2.

### Shortest Unsorted Continuous Subarray (Find boundary of disorder)
Walk forward tracking max - any element smaller than max is out of
order, update right boundary. Walk backward tracking min - any element
larger than min is out of order, update left boundary. Answer is
right minus left plus 1.

### Height Checker (Bubble sort copy, count mismatches)
Make a sorted copy using bubble sort. Compare each position with
original. Count positions where they differ. Those are the students
not standing in the right place.

### Relative Sort Array (Hashmap count, place by arr2 order, sort rest)
Count frequencies of all arr1 elements. Place elements in the order
they appear in arr2 using their counts. Collect remaining elements
not in arr2, sort them with bubble sort, append to result.