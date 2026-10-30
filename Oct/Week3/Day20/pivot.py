# Problem: Find Pivot Index
# Pattern: Prefix sum - left sum equals right sum at pivot
# Time: O(n) | Space: O(1)
# DON'T use sum(nums[:i]) inside loop - that's O(n^2)

def pivotIndex(nums):
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

print(pivotIndex([1,7,3,6,5,6]))   # 3
print(pivotIndex([1,2,3]))          # -1
print(pivotIndex([2,1,-1]))         # 0