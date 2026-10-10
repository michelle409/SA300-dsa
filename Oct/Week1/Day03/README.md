# Day 03 - Single Number
**Topic:** XOR bit trick

## Primary: Single Number
**Approach:** XOR all numbers together. Every number that appears twice
cancels itself out because a XOR a = 0. The single number is left
standing because a XOR 0 = a. One pass, no extra space.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Single element array - XOR with 0 gives the
number itself, returns correctly.

## Variants

### Single Number II (Bit counting)
Every number appears 3 times except one. Count the 1 bits at each
of the 32 bit positions across all numbers. If count at a position
is not divisible by 3, the single number has a 1 there. O(n) time,
O(1) space.

### Single Number III (XOR with partition)
Two single numbers exist. XOR everything to get a XOR b. Find a bit
where a and b differ using diff_bit = xor and (-xor). Use that bit
to split array into two groups. XOR each group separately to get
each single number. O(n) time, O(1) space.

### Missing Number (XOR expected range vs actual)
XOR all indices from 0 to n against all values in the array. Pairs
cancel, the missing number remains. O(n) time, O(1) space.

### Find the Difference (XOR chars from both strings)
Convert each character to a number using ord(). XOR all characters
from both strings. Every character in s appears in t so they cancel.
The extra character remains. Convert back with chr(). O(n) time,
O(1) space.