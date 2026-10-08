# Problem: Contains Duplicate
# Pattern: Set membership - check if seen before
# Time: O(n) | Space: O(n)

def containsDuplicate(nums):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False

print(containsDuplicate([1, 2, 3, 1]))   # True
print(containsDuplicate([1, 2, 3, 4]))   # False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True