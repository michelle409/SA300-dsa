# Problem: Element Appearing More Than 25% In Sorted Array
# Pattern: Sorted array - check element against element n//4 ahead
# Time: O(n) | Space: O(1)

def findSpecialInteger(arr):
    n = len(arr)
    quarter = n // 4
    for i in range(n - quarter):
        if arr[i] == arr[i + quarter]:
            return arr[i]

print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))  # 6
print(findSpecialInteger([1,1]))                   # 1