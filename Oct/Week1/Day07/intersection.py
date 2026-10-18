# Problem: Intersection of Two Arrays II
# Pattern: Hashmap counting - build freq dict for nums1, walk nums2
# Time: O(n+m) | Space: O(n)
# DON'T use Counter or & operator - build two dicts manually

def intersect(nums1, nums2):
    count = {}
    for i in range(len(nums1)):
        if nums1[i] in count:
            count[nums1[i]] = count[nums1[i]] + 1
        else:
            count[nums1[i]] = 1

    result = []
    for i in range(len(nums2)):
        if nums2[i] in count and count[nums2[i]] > 0:
            result.append(nums2[i])
            count[nums2[i]] = count[nums2[i]] - 1

    return result

print(intersect([1,2,2,1], [2,2]))          # [2,2]
print(intersect([4,9,5], [9,4,9,8,4]))      # [4,9]