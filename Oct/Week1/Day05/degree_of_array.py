# Problem: Degree of an Array
# Pattern: Hashmap - track count, first index, last index per number
# Time: O(n) | Space: O(n)

def findShortestSubArray(nums):
    count = {}
    first = {}
    last = {}

    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 0
            first[nums[i]] = i
        count[nums[i]] = count[nums[i]] + 1
        last[nums[i]] = i

    degree = 0
    for num in count:
        if count[num] > degree:
            degree = count[num]

    result = len(nums)
    for num in count:
        if count[num] == degree:
            length = last[num] - first[num] + 1
            if length < result:
                result = length

    return result

print(findShortestSubArray([1,2,2,3,1]))        # 2
print(findShortestSubArray([1,2,2,3,1,4,2]))    # 6