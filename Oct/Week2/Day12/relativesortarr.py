# Problem: Relative Sort Array
# Pattern: Hashmap - count frequencies, place in order of arr1, then remaining sorted
# Time: O(n) | Space: O(n)

def relativeSortArray(arr1, arr2):
    count = {}
    for i in range(len(arr1)):
        if arr1[i] in count:
            count[arr1[i]] = count[arr1[i]] + 1
        else:
            count[arr1[i]] = 1

    result = []

    for i in range(len(arr2)):
        for j in range(count[arr2[i]]):
            result.append(arr2[i])
        count[arr2[i]] = 0

    remaining = []
    for key in count:
        if count[key] > 0:
            for j in range(count[key]):
                remaining.append(key)

    n = len(remaining)
    for i in range(n):
        for j in range(n - 1):
            if remaining[j] > remaining[j + 1]:
                remaining[j], remaining[j + 1] = remaining[j + 1], remaining[j]

    return result + remaining

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))