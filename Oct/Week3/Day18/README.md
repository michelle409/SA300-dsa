# Day 18 - Reverse Words in a String III
**Topic:** String split + in-place word reversal

## Primary: Reverse Words in a String III
**Approach:** Convert string to list. Walk through finding word
boundaries (space or end of string). When a boundary is found reverse
the word from start to boundary-1 using two pointer swap. Update start
to character after the space. Spaces stay in place.

**Time:** O(n) | **Space:** O(n)

**Edge case I caught:** Loop goes to len(chars)+1 not len(chars) so
the last word (which has no trailing space) also gets reversed when i
hits the end.

## Variants

### Reverse Words in a String (Reverse word order not letters)
Split by spaces (handles multiple spaces automatically). Two pointer
swap the words list to reverse the order. Rejoin with single spaces.

### Reverse Only Letters (Two pointers skip non-letters)
Same two pointer structure as primary. Skip non-letter characters on
both sides using isalpha(). Swap only letters. Non-letters stay frozen
in their original positions.

### Length of Last Word (Scan from end)
Start from the end. Skip trailing spaces first. Then count characters
until you hit another space or the start. Return the count.

### To Lower Case (ASCII arithmetic)
Uppercase letters are ASCII 65-90. Adding 32 to the ASCII value of any
uppercase letter gives its lowercase equivalent. Walk through converting
each uppercase char manually without s.lower().

### String Compression (Read-write two pointers)
Read pointer finds each character and counts consecutive occurrences.
Write pointer writes the character then the count digits back in place.
Count is only written if greater than 1. Return write position as new
length.