# Problem: Contains Duplicate II
# Pattern: Sliding window + set - maintain window of size k
# Time: O(n) | Space: O(k)
# Different from Day 2 approach - using sliding window set not dict

def containsNearbyDuplicate(nums, k):
    window = set()
    left = 0

    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left = left + 1
        if nums[right] in window:
            return True
        window.add(nums[right])

    return False

print(containsNearbyDuplicate([1,2,3,1], 3))      # True
print(containsNearbyDuplicate([1,0,1,1], 1))       # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))   # False