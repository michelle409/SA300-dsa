# Problem: Find All Numbers Disappeared in an Array
# Pattern: In-place marking - negate value at home position
# Time: O(n) | Space: O(1)

def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
print(findDisappearedNumbers([1,1]))                # [2]