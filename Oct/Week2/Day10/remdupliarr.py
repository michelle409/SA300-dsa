# Problem: Remove Duplicates from Sorted Array
# Pattern: Two pointers - read pointer and write pointer
# Time: O(n) | Space: O(1) - in place
# DON'T use list(set(nums)) or list(dict.fromkeys(nums))

def removeDuplicates(nums):
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write = write + 1
    return write

print(removeDuplicates([1,1,2]))                    # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))     # 5