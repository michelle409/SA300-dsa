# Problem: Next Greater Element I
# Pattern: Monotonic decreasing stack + hashmap
# Time: O(n+m) | Space: O(n)
# DON'T use bisect - plain list as monotonic stack

def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []
    for i in range(len(nums2)):
        while len(stack) > 0 and stack[len(stack)-1] < nums2[i]:
            next_greater[stack.pop()] = nums2[i]
        stack.append(nums2[i])
    while len(stack) > 0:
        next_greater[stack.pop()] = -1

    result = []
    for i in range(len(nums1)):
        result.append(next_greater[nums1[i]])
    return result

print(nextGreaterElement([4,1,2], [1,3,4,2]))   # [-1,3,-1]
print(nextGreaterElement([2,4], [1,2,3,4]))      # [3,-1]