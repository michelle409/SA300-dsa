# Problem: Shortest Unsorted Continuous Subarray
# Pattern: Find boundaries of unsorted section
# Time: O(n) | Space: O(1)

def findUnsortedSubarray(nums):
    n = len(nums)
    left = -1
    right = -1
    max_val = nums[0]
    min_val = nums[n - 1]

    for i in range(1, n):
        if nums[i] < max_val:
            right = i
        else:
            max_val = nums[i]

    for i in range(n - 2, -1, -1):
        if nums[i] > min_val:
            left = i
        else:
            min_val = nums[i]

    if right == -1:
        return 0
    return right - left + 1

print(findUnsortedSubarray([2,6,4,8,10,9,15]))  # 5
print(findUnsortedSubarray([2,3,3,2,4]))         # 3
print(findUnsortedSubarray([1,2,3,4]))            # 0