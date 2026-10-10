# Problem: Single Number
# Pattern: XOR - pairs cancel out, single number remains
# Time: O(n) | Space: O(1)

def singleNumber(nums):
    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]
    return result

print(singleNumber([2, 2, 1]))        # 1
print(singleNumber([4, 1, 2, 1, 2])) # 4
print(singleNumber([1]))              # 1