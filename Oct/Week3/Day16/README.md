# Day 16 - Longest Palindromic Substring
**Topic:** String expand around center + two pointer patterns

## Primary: Longest Palindromic Substring
**Approach:** For each character expand outward in both directions as
long as characters match. Do this twice — once for odd length (single
char center) and once for even length (two char center). Track the
longest palindrome found. Return it after checking all positions.

**Time:** O(n^2) | **Space:** O(1)

**Edge case I caught:** After expanding, left overshot by 1 and right
overshot by 1. So the actual palindrome is s[left+1:right] not
s[left:right+1].

## Variants

### Valid Palindrome (Two pointers - skip non-alphanumeric inline)
Left pointer at start, right at end. Skip non-alphanumeric on both
sides. Compare lowercase characters. Return False on first mismatch.
Return True if pointers meet without mismatch.

### Count and Say (String simulation - read and encode)
Start with "1". Each term describes the previous term. Walk through
previous term counting consecutive same digits. Append count then
digit. Build new string. Repeat n-1 times.

### String Compression (Two pointers read-write in place)
Read pointer finds each character and counts consecutive occurrences.
Write pointer writes the character then the count (if > 1) back into
the array in place. Return write pointer position as new length.

### Isomorphic Strings (Two hashmaps - map both directions)
Map each character in s to its corresponding character in t AND map
each character in t back to s. If any mapping conflicts return False.
Need both directions because "foo" to "bar" would pass with one map
but fails with two.