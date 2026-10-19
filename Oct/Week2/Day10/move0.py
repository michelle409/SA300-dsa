# Problem: Move Zeroes
# Pattern: Two pointers - write non-zeros forward, fill rest with zeros
# Time: O(n) | Space: O(1) - in place
# DON'T use sort or filter

def moveZeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write = write + 1
    while write < len(nums):
        nums[write] = 0
        write = write + 1

nums1 = [0,1,0,3,12]
moveZeroes(nums1)
print(nums1)  # [1,3,12,0,0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # [0]