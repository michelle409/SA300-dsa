# Day 31 - Backspace String Compare
**Topic:** Stack simulation revisit

## Primary: Backspace String Compare
**Approach:** Process each string with a stack. Regular chars push.
Hash pops if stack non-empty. Compare the two resulting stacks.
Helper function keeps it clean.

**Time:** O(n+m) | **Space:** O(n+m)

**Edge case I caught:** Only pop if stack is non-empty. Backspace on
empty string does nothing.

## Variants

### Simplify Path (Stack process path components)
Split by slash. Skip empty strings and dots. Pop on double-dot if
stack non-empty. Push valid directory names. Join with slashes.

### Remove All Adjacent Duplicates (See Day 23)
Already covered.

### Remove K Digits (Monotonic stack greedy)
Walk digits maintaining monotonic increasing stack. When current
digit is smaller than top and k>0 pop the top (removes a larger
digit). After loop if k remaining pop from end. Strip leading zeros.

### Reverse Only Letters (See Day 18)
Already covered.

### Decoded String at Index (Work backwards with modulo)
First pass compute total decoded length. Second pass work backwards
using k%length to find position in current level. Return char when
k becomes 0 at a letter position.