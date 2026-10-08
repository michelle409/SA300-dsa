# Problem: 3Sum
# Pattern: Sort + fix one number + two pointers on the rest
# Time: O(n^2) | Space: O(n)

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left = left + 1
                right = right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left = left + 1
                while left < right and nums[right] == nums[right + 1]:
                    right = right - 1
            elif total < 0:
                left = left + 1
            else:
                right = right - 1
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0]))
print(threeSum([0, 1, 1]))