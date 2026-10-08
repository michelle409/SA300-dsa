# Problem: 3Sum Closest
# Pattern: Sort + fix one + two pointers, track closest distance
# Time: O(n^2) | Space: O(1)

def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total == target:
                return total
            elif total < target:
                left = left + 1
            else:
                right = right - 1
    return closest

print(threeSumClosest([-1, 2, 1, -4], 1))   # 2
print(threeSumClosest([0, 0, 0], 1))          # 0