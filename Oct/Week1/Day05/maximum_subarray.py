# Problem: Maximum Subarray
# Pattern: Kadane's Algorithm - extend or restart subarray
# Time: O(n) | Space: O(1)

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        if current_sum + nums[i] > nums[i]:
            current_sum = current_sum + nums[i]
        else:
            current_sum = nums[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArray([1]))                        # 1
print(maxSubArray([5,4,-1,7,8]))              # 23