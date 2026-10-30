# Problem: Minimum Value to Get Positive Step by Step Sum
# Pattern: Prefix sum - track running minimum
# Time: O(n) | Space: O(1)

def minStartValue(nums):
    min_sum = 0
    running = 0
    for i in range(len(nums)):
        running = running + nums[i]
        if running < min_sum:
            min_sum = running
    return 1 - min_sum

print(minStartValue([-3,2,-3,4,2]))  # 5
print(minStartValue([1,2]))           # 1
print(minStartValue([1,-2,-3]))       # 5