# Problem: Next Greater Element II
# Pattern: Monotonic stack - circular array double pass
# Time: O(n) | Space: O(n)

def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2 * n):
        while len(stack) > 0 and nums[stack[len(stack)-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)
    return result

print(nextGreaterElements([1,2,1]))    # [2,-1,2]
print(nextGreaterElements([1,2,3,4,3]))  # [2,3,4,-1,4]