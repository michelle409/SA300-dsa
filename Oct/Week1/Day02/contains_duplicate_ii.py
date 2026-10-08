# Problem: Contains Duplicate II
# Pattern: Hashmap - store last seen index, check distance
# Time: O(n) | Space: O(n)

def containsNearbyDuplicate(nums, k):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return True
        seen[nums[i]] = i
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))      # True
print(containsNearbyDuplicate([1,0,1,1], 1))       # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  # False