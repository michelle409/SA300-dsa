# Day 08 - Valid Palindrome
**Topic:** Two pointers from both ends

## Primary: Valid Palindrome
**Approach:** Left pointer at start, right pointer at end. Skip non-alphanumeric
characters on both sides inline during the walk - no cleanup before starting.
Compare characters after converting to lowercase. If they don't match return
False. If pointers meet without a mismatch return True.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Empty string after removing non-alphanumeric characters
returns True. The while left < right condition handles this naturally since
the pointers never enter the loop.

## Variants

### Valid Palindrome II (Two pointers - one skip allowed on mismatch)
Same two pointer walk but on first mismatch you get one chance. Try
skipping the left character or skipping the right character. Check if
either remaining substring is a palindrome using a helper function.
If either returns True the string is valid.

### Palindrome Number (Reverse number mathematically - no string conversion)
Negative numbers are never palindromes. Numbers ending in 0 (except 0
itself) are never palindromes. Reverse the number digit by digit using
modulo and division. Compare reversed number with original.

### Palindromic Substrings (Expand around center - count all palindromes)
For each character expand outward in both directions as long as characters
match. Each successful expansion is one palindromic substring. Do this
twice per index - once for odd length (single char center) and once for
even length (two char center). Sum all counts.

### Reverse Only Letters (Two pointers - skip non-letters, swap letters only)
Same two pointer structure as primary. Skip non-letter characters on both
sides using isalpha(). Swap only letters. Non-letters stay in their
original positions. Convert string to list first since strings are
immutable in Python.