# Problem: Sort Colors
# Pattern: Dutch National Flag - three pointers low mid high
# Time: O(n) | Space: O(1) - in place, no sort function
# low tracks where next 0 goes
# high tracks where next 2 goes
# mid is the current element being examined

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low = low + 1
            mid = mid + 1
        elif nums[mid] == 1:
            mid = mid + 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high = high - 1

nums1 = [2,0,2,1,1,0]
sortColors(nums1)
print(nums1)  # [0,0,1,1,2,2]

nums2 = [2,0,1]
sortColors(nums2)
print(nums2)  # [0,1,2]