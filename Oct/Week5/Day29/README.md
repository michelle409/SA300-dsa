# Day 29 - Best Time to Buy and Sell Stock
**Topic:** Single pass greedy - track running minimum

## Primary: Best Time to Buy and Sell Stock
**Approach:** Track the minimum price seen so far. At each price
calculate profit if selling today. Update max profit if better.
Never look back - one pass does it all.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Start max_profit at 0 not -infinity. If no
profit is possible the answer is 0 (don't trade).

## Variants

### Best Time II (Multiple transactions - greedy sum of gains)
Take every upward move. If today is higher than yesterday add the
difference. This captures all profitable sequences.

### Maximum Subarray (See Pattern G - Kadane)
Already covered.

### Best Time with Cooldown (State machine three states)
Three states: held (own stock), sold (just sold must rest), rest
(resting). Transition each state on every day. Answer is max of
sold and rest at the end.