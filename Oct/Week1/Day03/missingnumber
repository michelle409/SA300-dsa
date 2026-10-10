# Problem: Missing Number
# Pattern: XOR - XOR expected range against actual array
# Time: O(n) | Space: O(1)

def missingNumber(nums):
    result = len(nums)
    for i in range(len(nums)):
        result = result ^ i ^ nums[i]
    return result

print(missingNumber([3, 0, 1]))              # 2
print(missingNumber([0, 1]))                 # 2
print(missingNumber([9,6,4,2,3,5,7,0,1]))   # 8