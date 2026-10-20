# Problem: Longest Continuous Subarray With Absolute Diff <= Limit
# Pattern: Sliding window - shrink when max-min > limit
# Time: O(n^2) | Space: O(1)
# Note: optimal uses deque but we build manually without collections

def longestSubarray(nums, limit):
    left = 0
    max_len = 0

    for right in range(len(nums)):
        # find max and min in current window manually
        cur_max = nums[left]
        cur_min = nums[left]
        for i in range(left, right + 1):
            if nums[i] > cur_max:
                cur_max = nums[i]
            if nums[i] < cur_min:
                cur_min = nums[i]

        while cur_max - cur_min > limit:
            left = left + 1
            cur_max = nums[left]
            cur_min = nums[left]
            for i in range(left, right + 1):
                if nums[i] > cur_max:
                    cur_max = nums[i]
                if nums[i] < cur_min:
                    cur_min = nums[i]

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len

print(longestSubarray([8,2,4,7], 4))       # 2
print(longestSubarray([10,1,2,4,7,2], 5))  # 4
print(longestSubarray([4,2,2,2,4,4,2,2], 0))  # 3