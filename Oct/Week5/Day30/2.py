# Problem: Partition Array According to Given Pivot
# Pattern: Three-pass - less than, equal, greater than pivot
# Time: O(n) | Space: O(n)

def pivotArray(nums, pivot):
    less = []
    equal = []
    greater = []
    for i in range(len(nums)):
        if nums[i] < pivot:
            less.append(nums[i])
        elif nums[i] == pivot:
            equal.append(nums[i])
        else:
            greater.append(nums[i])
    return less + equal + greater

print(pivotArray([9,12,5,10,14,3,10], 10))  # [9,5,3,10,10,12,14]
print(pivotArray([-3,4,3,2], 2))             # [-3,2,4,3]