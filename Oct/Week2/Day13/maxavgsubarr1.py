# Problem: Maximum Average Subarray I
# Pattern: Fixed size sliding window - add one subtract one keep running sum
# Time: O(n) | Space: O(1)
# DON'T use sum(nums[i:i+k]) inside loop - that's O(n*k)

def findMaxAverage(nums, k):
    window_sum = 0
    for i in range(k):
        window_sum = window_sum + nums[i]

    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
print(findMaxAverage([5], 1))                  # 5.0