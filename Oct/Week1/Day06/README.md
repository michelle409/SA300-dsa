# Day 06 - Find All Numbers Disappeared in an Array
**Topic:** In-place marking (array as hashmap)

## Primary: Find All Numbers Disappeared in an Array
**Approach:** Walk through the array. For each number go to position
abs(nums[i]) - 1 and negate the value there to mark it as visited.
After one pass, any position still positive means that index+1 never
appeared in the array. Collect those into result.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Values might already be negative from a previous
marking so I use abs(nums[i]) to get the true index every time.

## Variants

### First Missing Positive (In-place marking with out-of-range cleanup)
Values outside range 1 to n are useless so replace them with n+1 first.
Then apply same negation trick. First position still positive after both
passes gives the answer. Return n+1 if all positions are negative.

### Set Mismatch (In-place marking - find duplicate and missing together)
Walk through and negate at home position. If home is already negative
that number is the duplicate. After the pass, position still positive
gives the missing number. Returns both in one array.

### Missing Number (Math - sum formula, different from Day 3 XOR approach)
Expected sum of 0 to n is n*(n+1)/2. Subtract actual sum of array.
The difference is the missing number. Showing two approaches to the
same problem - XOR in Day 3, math formula here.

### Find All Duplicates in an Array (In-place marking - revisited from Day 2)
Same pattern as primary. Go to home position abs(nums[i])-1. If already
negative that number appeared twice - add to result. Otherwise negate
to mark visited. Reinforces the in-place marking pattern.