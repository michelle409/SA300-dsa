# Problem: Majority Element
# Topic: Hashmap counting + Boyer-Moore Voting Algorithm
# Day 5 - Primary

# ---- SOLUTION 1: Hashmap O(n) time O(n) space ----
# Count frequency of each number, return the one > n/2
def majorityElement_hashmap(nums):
    count = {}
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] = count[nums[i]] + 1
        else:
            count[nums[i]] = 1
        if count[nums[i]] > len(nums) // 2:
            return nums[i]

# ---- SOLUTION 2: Boyer-Moore Voting O(n) time O(1) space ----
# Candidate survives cancellation because majority > n/2
def majorityElement_boyermoore(nums):
    candidate = None
    count = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
        if nums[i] == candidate:
            count = count + 1
        else:
            count = count - 1
    return candidate

# Tests
print(majorityElement_hashmap([3, 2, 3]))             # 3
print(majorityElement_hashmap([2, 2, 1, 1, 1, 2, 2])) # 2

print(majorityElement_boyermoore([3, 2, 3]))             # 3
print(majorityElement_boyermoore([2, 2, 1, 1, 1, 2, 2])) # 2