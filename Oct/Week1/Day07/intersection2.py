# Problem: Intersection of Two Arrays
# Pattern: Set membership - unique intersection only
# Time: O(n+m) | Space: O(n)

def intersection(nums1, nums2):
    seen = set()
    for i in range(len(nums1)):
        seen.add(nums1[i])

    result = set()
    for i in range(len(nums2)):
        if nums2[i] in seen:
            result.add(nums2[i])

    return list(result)

print(intersection([1,2,2,1], [2,2]))        # [2]
print(intersection([4,9,5], [9,4,9,8,4]))    # [9,4]