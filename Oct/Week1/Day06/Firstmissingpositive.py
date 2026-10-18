# Problem: First Missing Positive
# Pattern: In-place marking - same as Find Disappeared but find smallest missing
# Time: O(n) | Space: O(1)

def firstMissingPositive(nums):
    n = len(nums)

    # Step 1 - mark out of range values as n+1 (irrelevant)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2 - negate at home position for values in range 1 to n
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]

    # Step 3 - first positive position is the answer
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1

print(firstMissingPositive([1,2,0]))        # 3
print(firstMissingPositive([3,4,-1,1]))     # 2
print(firstMissingPositive([7,8,9,11,12]))  # 1