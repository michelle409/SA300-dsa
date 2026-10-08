# Problem: Find All Duplicates in an Array
# Pattern: In-place marking - use index as hashmap, negate to mark visited
# Time: O(n) | Space: O(1)

def findDuplicates(nums):
    result = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            result.append(abs(nums[i]))
        else:
            nums[index] = -nums[index]
    return result

print(findDuplicates([4,3,2,7,8,2,3,1]))  # [2, 3]
print(findDuplicates([1,1,2]))             # [1]
print(findDuplicates([1]))                 # []