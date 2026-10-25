# Day 15 - Valid Anagram
**Topic:** String hashmap frequency counting

## Primary: Valid Anagram
**Approach:** Build frequency count of all characters in s. Walk through
t and decrement count for each character. If a character doesn't exist
or count hits 0 before t is done return False. If lengths differ return
False immediately.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Check length first. If lengths differ they can
never be anagrams — no need to count anything.

## Variants

### First Unique Character in a String (Two pass - count then find)
First pass build frequency count of all characters. Second pass walk
through string in order and return index of first character with
count equal to 1. Return -1 if none found.

### Ransom Note (Hashmap - count magazine, check ransomNote)
Count all characters in magazine. Walk through ransomNote checking
each character exists in count and has remaining uses. Decrement
each time you use one. Return False if any character missing or
exhausted. Same pattern as Valid Anagram second loop.

### Group Anagrams (Sort each word as key, group same keys)
Sort each word using bubble sort to get its canonical form. Use
sorted word as dict key. Append original word to that key's group.
Words that are anagrams of each other will have the same sorted form
and end up in the same group.

### Longest Common Prefix (Vertical scanning - column by column)
Take first string as reference. Walk column by column (same position
across all strings). If any string is shorter or has a different
character at that position return everything before that position.