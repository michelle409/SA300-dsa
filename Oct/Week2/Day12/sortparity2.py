# Problem: Sort Array By Parity II
# Pattern: Two pointers - even index gets even number, odd index gets odd
# Time: O(n) | Space: O(n)

def sortArrayByParityII(nums):
    result = [0] * len(nums)
    even = 0
    odd = 1
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result[even] = nums[i]
            even = even + 2
        else:
            result[odd] = nums[i]
            odd = odd + 2
    return result

print(sortArrayByParityII([4,2,5,7]))  # [4,5,2,7]
print(sortArrayByParityII([2,3]))       # [2,3]