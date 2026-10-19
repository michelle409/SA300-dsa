# Problem: Merge Intervals
# Pattern: Sort by start + merge overlapping intervals
# Time: O(n log n) | Space: O(n)

def merge(intervals):
    # sort by start time using bubble sort
    n = len(intervals)
    for i in range(n):
        for j in range(n - 1):
            if intervals[j][0] > intervals[j + 1][0]:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]

    result = [intervals[0]]

    for i in range(1, len(intervals)):
        last = result[len(result) - 1]
        if intervals[i][0] <= last[1]:
            if intervals[i][1] > last[1]:
                last[1] = intervals[i][1]
        else:
            result.append(intervals[i])

    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                  # [[1,5]]