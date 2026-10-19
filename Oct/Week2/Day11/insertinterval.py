# Problem: Insert Interval
# Pattern: Three phases - before overlap, merge overlap, after overlap
# Time: O(n) | Space: O(n)

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # phase 1 - add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i = i + 1

    # phase 2 - merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        if intervals[i][0] < newInterval[0]:
            newInterval[0] = intervals[i][0]
        if intervals[i][1] > newInterval[1]:
            newInterval[1] = intervals[i][1]
        i = i + 1
    result.append(newInterval)

    # phase 3 - add remaining intervals
    while i < n:
        result.append(intervals[i])
        i = i + 1

    return result

print(insert([[1,3],[6,9]], [2,5]))              # [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]