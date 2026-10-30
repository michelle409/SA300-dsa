# Day 22 - Valid Parentheses
**Topic:** Stack - push open pop and match on close

## Primary: Valid Parentheses
**Approach:** Push every open bracket onto the stack. On every close
bracket check if stack top is the matching open. If not or stack empty
return False. After full scan stack must be empty.

**Time:** O(n) | **Space:** O(n)

**Edge case I caught:** Empty stack when a close bracket arrives means
there's nothing to match it with - return False immediately.

## Variants

### Minimum Add to Make Valid (Count unmatched open and close)
Track unmatched open brackets with a counter. On close bracket if
open_count > 0 it matches so decrement. Otherwise increment
close_count. Answer is open_count + close_count.

### Remove Outermost Parentheses (Depth counter skip outer layer)
Track nesting depth. Only add characters to result when depth > 0
for open or depth > 1 for close. The outermost layer is depth 0 to 1.

### Score of Parentheses (Stack of running scores per depth)
Stack holds running score at each depth. Open pushes 0. Close pops
val - if 0 (empty pair) add 1 to top, else add 2*val (nested pair).

### Minimum Remove to Make Valid (Track indices of unmatched)
Stack stores indices of unmatched open brackets. On unmatched close
blank it immediately. After loop blank all remaining stack indices.