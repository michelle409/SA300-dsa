# Problem: Continuous Subarray Sum
# Pattern: Prefix sum mod + hashmap
# Time: O(n) | Space: O(n)

def checkSubarraySum(nums, k):
    seen = {0: -1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum = prefix_sum + nums[i]
        mod = prefix_sum % k
        if mod in seen:
            if i - seen[mod] >= 2:
                return True
        else:
            seen[mod] = i
    return False

print(checkSubarraySum([23,2,4,6,7], 6))   # True
print(checkSubarraySum([23,2,6,4,7], 6))   # True
print(checkSubarraySum([23,2,6,4,7], 13))  # False