# Problem: Single Number II
# Pattern: Bit counting - count 1s at each bit position, mod 3
# Time: O(n) | Space: O(1)

def singleNumber(nums):
    result = 0
    for bit in range(32):
        count = 0
        for i in range(len(nums)):
            if (nums[i] >> bit) & 1:
                count += 1
        if count % 3 != 0:
            result = result | (1 << bit)
    if result >= 2**31:
        result -= 2**32
    return result

print(singleNumber([2, 2, 3, 2]))        # 3
print(singleNumber([0,1,0,1,0,1,99]))    # 99