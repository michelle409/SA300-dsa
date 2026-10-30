# Day 27 - Implement Queue using Stacks
**Topic:** Two-stack FIFO simulation

## Primary: Implement Queue using Stacks
**Approach:** Two stacks - in_stack for push, out_stack for pop/peek.
Transfer all elements from in_stack to out_stack only when out_stack
is empty. This reversal gives FIFO order. Amortized O(1) because each
element moves at most twice.

**Time:** O(1) amortized | **Space:** O(n)

**Edge case I caught:** Only transfer when out_stack is empty not on
every pop. If you transfer every time you lose the correct order.

## Variants

### Implement Stack using Queues (Rotate queue on push)
After pushing new element rotate all previous elements to the back.
The newest element is always at the front giving LIFO behavior.

### Design Circular Queue (Fixed array with head/tail pointers)
Fixed size array. Head and tail pointers move forward with modulo
wrapping. Size counter tracks how many elements exist.

### Moving Average (Queue window with running sum)
Fixed size queue. When full remove oldest element and subtract from
sum before adding new. Divide sum by current size for average.