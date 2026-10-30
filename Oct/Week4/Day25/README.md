# Day 25 - Min Stack
**Topic:** Augmented stack - carry extra state alongside primary stack

## Primary: Min Stack
**Approach:** Two stacks. Main stack stores all values normally.
Min stack stores minimums — only push when new value is <= current
minimum. On pop if popped value equals min stack top pop min stack too.
getMin is always O(1) — just peek min stack top.

**Time:** O(1) all ops | **Space:** O(n)

**Edge case I caught:** Use <= not < when pushing to min stack.
Duplicate minimums need to be tracked separately so popping one
doesn't lose the minimum.

## Variants

### Online Stock Span (Monotonic stack accumulate spans)
Stack stores [price, span] pairs. On each new price pop all smaller
or equal prices accumulating their spans. Push current price with
accumulated span.

### Validate Stack Sequences (Simulate push/pop with two pointers)
Push all pushed elements one by one. After each push check if top
matches current popped element — if yes pop and advance popped pointer.
At the end stack should be empty.