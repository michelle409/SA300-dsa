# Problem: Remove Element
# Pattern: Two pointers - write pointer only moves when value != val
# Time: O(n) | Space: O(1)

def removeElement(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write = write + 1
    return write

print(removeElement([3,2,2,3], 3))          # 2
print(removeElement([0,1,2,2,3,0,4,2], 2))  # 5