# Problem: Minimum Size Subarray Sum
# Pattern: Variable sliding window - shrink from left when sum >= target
# Time: O(n) | Space: O(1)

def minSubArrayLen(target, nums):
    left = 0
    window_sum = 0
    min_len = len(nums) + 1

    for right in range(len(nums)):
        window_sum = window_sum + nums[right]
        while window_sum >= target:
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
            window_sum = window_sum - nums[left]
            left = left + 1

    if min_len == len(nums) + 1:
        return 0
    return min_len

print(minSubArrayLen(7, [2,3,1,2,4,3]))  # 2
print(minSubArrayLen(4, [1,4,4]))         # 1
print(minSubArrayLen(11, [1,1,1,1,1]))   # 0