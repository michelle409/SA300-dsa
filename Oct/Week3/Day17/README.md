# Day 17 - Longest Common Prefix
**Topic:** Vertical scan + string pattern matching

## Primary: Longest Common Prefix
**Approach:** Take the first string as reference. Walk column by column
(same position across all strings). If any string is shorter or has a
different character at that position return everything before that
position. If first string is fully scanned without mismatch return it.

**Time:** O(n*m) | **Space:** O(1)

**Edge case I caught:** If a string is shorter than the current index i,
return immediately — i >= len(strs[j]) handles this.

## Variants

### Find Common Characters (Min frequency across all words)
Build freq dict of first word as baseline. For each other word update
baseline to keep minimum counts. Characters missing from any word get
count 0. Build result repeating each char its minimum count times.

### Check If Word Occurs As Prefix (Word by word prefix match)
Split sentence by spaces. For each word manually check if searchWord
matches the start character by character. Return 1-based index of first
match. Return -1 if none found.

### Rotate String (Doubled string contains goal)
Concatenate s with itself. Any rotation of s appears as a substring of
s+s. Manually check if goal appears anywhere in the doubled string.

### Buddy Strings (Exactly two differing positions that swap)
Collect positions where s and goal differ. If 0 diffs need a duplicate
char in s (can swap same chars). If exactly 2 diffs check if swapping
those positions makes them equal. More than 2 diffs returns False.

### Repeated Substring Pattern (Try all valid pattern lengths)
Try every length from 1 to n//2 that divides n evenly. For each length
check if repeating that prefix covers the whole string. Return True on
first match.