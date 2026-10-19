# Day 13 - Maximum Average Subarray I
**Topic:** Fixed-size sliding window

## Primary: Maximum Average Subarray I
**Approach:** Build the first window of size k by summing the first k
elements. Then slide the window one step at a time - add the new right
element and subtract the old left element. Track the maximum sum seen.
Divide by k at the end to get the average. One pass O(n).

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Starting with the first window sum and using it
as max_sum ensures correct comparison even if all elements are negative.

## Variants

### Max Sum Subarray of Size K (GFG - fixed window returns sum not average)
Identical to primary but returns the max sum directly without dividing
by k. Same sliding window pattern - add right element subtract left
element each step.

### Minimum Size Subarray Sum (Variable window - shrink when sum reaches target)
Expand window by adding right element. When sum reaches or exceeds
target record window length and shrink from left by subtracting and
moving left pointer right. Keep track of minimum length seen.

### Longest Substring Without Repeating Characters (Variable window + hashmap)
Expand right. When duplicate found move left to one past the last
seen position of that character. Store last seen index of each
character in a dict. Window size at each step is a candidate answer.

### Max Consecutive Ones III (Variable window - count zeros, shrink when too many)
Expand right counting zeros. When zero count exceeds k shrink from
left until zero count is back to k. Window size at each step is
the current valid window length.