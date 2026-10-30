# Problem: Find the Middle Index in Array
# Pattern: Same as pivot index - identical problem different name
# Time: O(n) | Space: O(1)

def findMiddleIndex(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum = left_sum + nums[i]
    return -1

print(findMiddleIndex([2,3,-1,8,4]))   # 3
print(findMiddleIndex([1,-1,4]))        # 2
print(findMiddleIndex([2,5]))           # -1