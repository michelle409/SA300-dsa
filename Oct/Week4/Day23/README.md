# Day 23 - Baseball Game
**Topic:** Stack as running state simulation

## Primary: Baseball Game
**Approach:** Stack stores all valid scores. C pops last. D doubles
last and pushes. + sums last two and pushes. Numbers convert to int
and push. Sum the stack at the end.

**Time:** O(n) | **Space:** O(n)

**Edge case I caught:** + needs the last TWO elements. Access
stack[-2] and stack[-1] — both must exist before applying +.

## Variants

### Build Array With Stack Operations (Simulate push/pop to match target)
Walk 1 to n. Always push. If current number is NOT in target pop
immediately. Stop when target is fully matched.

### Make The String Great (Stack collapse adjacent case pairs)
Push each char. Before pushing check if top is same letter different
case. If yes pop instead of push — they cancel. Result is remaining
stack joined.

### Final Prices With Special Discount (Monotonic stack next smaller)
Stack stores indices. For each price pop all stack indices where
stored price >= current price — current price is their discount.
Subtract and record. Push current index.

### Remove All Adjacent Duplicates (Stack pop on match)
Push each char. If top equals current char they're adjacent duplicates
— pop instead of push. They annihilate. Join remaining stack.