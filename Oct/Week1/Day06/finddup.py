# Problem: Find All Duplicates in an Array
# Pattern: In-place marking - same pattern as Day 2
# Revisiting here as Day 6 variant to reinforce in-place marking
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

print(findDuplicates([4,3,2,7,8,2,3,1]))  # [2,3]
print(findDuplicates([1,1,2]))             # [1]
print(findDuplicates([1]))                 # []