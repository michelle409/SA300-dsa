# Problem: 4Sum
# Pattern: Sort + fix two numbers + two pointers
# Time: O(n^3) | Space: O(n)

def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right + 1]:
                        right = right - 1
                elif total < target:
                    left = left + 1
                else:
                    right = right - 1
    return result

print(fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2, 2, 2, 2, 2], 8))        # [[2,2,2,2]]