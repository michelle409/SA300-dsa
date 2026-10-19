# Problem: Max Sum Subarray of Size K
# Pattern: Fixed sliding window - same as primary but returns sum not average
# Time: O(n) | Space: O(1)

def maxSumSubarray(nums, k):
    window_sum = 0
    for i in range(k):
        window_sum = window_sum + nums[i]

    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

print(maxSumSubarray([2,1,5,1,3,2], 3))  # 9
print(maxSumSubarray([2,3,4,1,5], 2))    # 7