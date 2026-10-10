# Problem: Single Number III
# Pattern: XOR - find two singles using a differentiating bit
# Time: O(n) | Space: O(1)

def singleNumber(nums):
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]
    
    # find rightmost bit that is 1 in xor
    diff_bit = xor & (-xor)
    
    a = 0
    for i in range(len(nums)):
        if nums[i] & diff_bit:
            a = a ^ nums[i]
    
    b = xor ^ a
    return [a, b]

print(singleNumber([1, 2, 1, 3, 2, 5]))  # [3, 5]
print(singleNumber([-1, 0]))              # [-1, 0]
print(singleNumber([0, 1]))               # [0, 1]