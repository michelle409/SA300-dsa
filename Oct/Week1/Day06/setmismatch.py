# Problem: Set Mismatch
# Pattern: In-place marking - find duplicate (already negative) and missing (still positive)
# Time: O(n) | Space: O(1)

def findErrorNums(nums):
    duplicate = -1
    missing = -1

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            duplicate = abs(nums[i])
        else:
            nums[index] = -nums[index]

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1

    return [duplicate, missing]

print(findErrorNums([1,2,2,4]))  # [2,3]
print(findErrorNums([1,1]))       # [1,2]