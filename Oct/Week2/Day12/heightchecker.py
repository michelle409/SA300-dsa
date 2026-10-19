# Problem: Height Checker
# Pattern: Sort copy using bubble sort, compare with original
# Time: O(n^2) | Space: O(n)

def heightChecker(heights):
    expected = list(heights)
    n = len(expected)
    for i in range(n):
        for j in range(n - 1):
            if expected[j] > expected[j + 1]:
                expected[j], expected[j + 1] = expected[j + 1], expected[j]

    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count = count + 1
    return count

print(heightChecker([1,1,4,2,1,3]))  # 3
print(heightChecker([5,1,2,3,4]))    # 5
print(heightChecker([1,2,3,4,5]))    # 0