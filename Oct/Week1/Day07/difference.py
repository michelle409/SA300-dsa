# Problem: Find the Difference of Two Arrays
# Pattern: Set membership - find elements in one set not in the other
# Time: O(n+m) | Space: O(n+m)

def findDifference(nums1, nums2):
    set1 = set()
    set2 = set()

    for i in range(len(nums1)):
        set1.add(nums1[i])
    for i in range(len(nums2)):
        set2.add(nums2[i])

    result1 = []
    result2 = []

    for num in set1:
        if num not in set2:
            result1.append(num)

    for num in set2:
        if num not in set1:
            result2.append(num)

    return [result1, result2]

print(findDifference([1,2,3], [2,4,6]))      # [[1,3],[4,6]]
print(findDifference([1,2,3,3], [1,1,2,2]))  # [[3],[]]