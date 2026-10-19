# Problem: Squares of a Sorted Array
# Pattern: Two pointers from both ends - biggest square always at one end
# Time: O(n) | Space: O(n)
# DON'T use sorted(x*x for x in nums) - that's O(n log n)

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result[pos] = left_sq
            left = left + 1
        else:
            result[pos] = right_sq
            right = right - 1
        pos = pos - 1

    return result

print(sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
print(sortedSquares([-7,-3,2,3,11]))  # [4,9,9,49,121]