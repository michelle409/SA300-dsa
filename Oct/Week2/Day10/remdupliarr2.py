# Problem: Remove Duplicates from Sorted Array II
# Pattern: Two pointers - allow at most 2 of each element
# Time: O(n) | Space: O(1)

def removeDuplicates(nums):
    write = 2
    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write = write + 1
    return write

print(removeDuplicates([1,1,1,2,2,3]))        # 5
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))  # 7