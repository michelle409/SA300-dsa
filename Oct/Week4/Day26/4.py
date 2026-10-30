# Problem: Largest Rectangle in Histogram
# Pattern: Monotonic increasing stack - find boundaries of each bar
# Time: O(n) | Space: O(n)

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights = heights + [0]
    for i in range(len(heights)):
        while len(stack) > 0 and heights[stack[len(stack)-1]] > heights[i]:
            h = heights[stack.pop()]
            if len(stack) == 0:
                w = i
            else:
                w = i - stack[len(stack)-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))  # 10
print(largestRectangleArea([2,4]))           # 4