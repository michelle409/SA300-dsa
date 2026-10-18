# Problem: Majority Element II
# Pattern: Extended Boyer-Moore with two candidates
# Time: O(n) | Space: O(1)

def majorityElement(nums):
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0

    # Phase 1 - find two candidates
    for i in range(len(nums)):
        if nums[i] == candidate1:
            count1 = count1 + 1
        elif nums[i] == candidate2:
            count2 = count2 + 1
        elif count1 == 0:
            candidate1 = nums[i]
            count1 = 1
        elif count2 == 0:
            candidate2 = nums[i]
            count2 = 1
        else:
            count1 = count1 - 1
            count2 = count2 - 1

    # Phase 2 - verify candidates actually appear > n/3 times
    result = []
    threshold = len(nums) // 3
    count1 = 0
    count2 = 0
    for i in range(len(nums)):
        if nums[i] == candidate1:
            count1 = count1 + 1
        elif nums[i] == candidate2:
            count2 = count2 + 1
    if count1 > threshold:
        result.append(candidate1)
    if count2 > threshold:
        result.append(candidate2)
    return result

print(majorityElement([3, 2, 3]))   # [3]
print(majorityElement([1]))          # [1]
print(majorityElement([1, 2]))       # [1, 2]