# Problem: Two Sum II - Input Array Is Sorted
# Pattern: Two pointers from both ends
# Time: O(n) | Space: O(1)

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left = left + 1
        else:
            right = right - 1

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))