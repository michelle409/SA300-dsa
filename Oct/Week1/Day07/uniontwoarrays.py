# Problem: Union of Two Arrays
# Pattern: Set membership - combine both arrays, keep unique values
# Time: O(n+m) | Space: O(n+m)

def unionArrays(nums1, nums2):
    seen = set()
    for i in range(len(nums1)):
        seen.add(nums1[i])
    for i in range(len(nums2)):
        seen.add(nums2[i])
    result = []
    for num in seen:
        result.append(num)
    return result

print(unionArrays([1,2,3,4,5], [1,2,3]))     # [1,2,3,4,5]
print(unionArrays([1,2,1,3,2], [2,3,4,5]))   # [1,2,3,4,5]