# Problem: Missing Number
# Pattern: Math - expected sum minus actual sum
# (Day 3 used XOR, this time using sum formula - different approach same problem)
# Time: O(n) | Space: O(1)

def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = 0
    for i in range(len(nums)):
        actual = actual + nums[i]
    return expected - actual

print(missingNumber([3,0,1]))              # 2
print(missingNumber([0,1]))                # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8