# Problem: Max Consecutive Ones III
# Pattern: Variable sliding window - allow at most k zeros
# Time: O(n) | Space: O(1)

def longestOnes(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros = zeros + 1
        while zeros > k:
            if nums[left] == 0:
                zeros = zeros - 1
            left = left + 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # 10