# Day 07 - Intersection of Two Arrays II
**Topic:** Hashmap counting + Set membership

## Primary: Intersection of Two Arrays II
**Approach:** Build a frequency dict for nums1. Walk through nums2 -
if a number exists in the dict with count greater than 0 it is in the
intersection. Add it to result and decrease the count so duplicates
are handled correctly.

**Time:** O(n+m) | **Space:** O(n)

**Edge case I caught:** Same number appearing multiple times - the count
decrement ensures we only include it as many times as it appears in
both arrays, not more.

## Variants

### intersection.py - Intersection of Two Arrays (Set membership)
Build a set from nums1. Walk nums2 and check if each element is in the
set. Use a result set to ensure uniqueness. Returns only unique common
elements unlike the primary which allows duplicates.

### common.py - Find Common Characters (Minimum frequency across all words)
Build frequency dict for first word. For each remaining word build its
own freq dict and keep the minimum count per character. Characters with
minimum count greater than 0 appear in all words. Add them to result
that many times.

### difference.py - Find the Difference of Two Arrays (Set difference)
Build a set from each array. Walk set1 and collect elements not in set2
into result1. Walk set2 and collect elements not in set1 into result2.
Returns two lists - what is unique to each array.

### uniontwoarrays.py - Union of Two Arrays (GFG - Set union)
Add all elements from both arrays into one set. Sets automatically
remove duplicates. Convert back to list and return. Gives all unique
elements that appear in either array.