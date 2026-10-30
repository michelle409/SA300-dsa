# Problem: Product of Array Except Self
# Pattern: Prefix product + suffix product in one pass
# Time: O(n) | Space: O(1) ignoring output

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

    return result

print(productExceptSelf([1,2,3,4]))      # [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]