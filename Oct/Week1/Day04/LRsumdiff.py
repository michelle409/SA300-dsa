# Problem: Left and Right Sum Differences
# Pattern: Prefix sum - build left and right sum arrays, find difference
# Time: O(n) | Space: O(n)

def leftRightDifference(nums):
    n = len(nums)
    
    left_sum = [0] * n
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]
    
    right_sum = [0] * n
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]
    
    answer = [0] * n
    for i in range(n):
        answer[i] = abs(left_sum[i] - right_sum[i])
    
    return answer

print(leftRightDifference([10,4,8,3]))  # [15,1,11,22]
print(leftRightDifference([1]))         # [0]