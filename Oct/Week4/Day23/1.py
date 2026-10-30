# Problem: Build Array With Stack Operations
# Pattern: Stack simulation - push/pop to build target
# Time: O(n) | Space: O(n)

def buildArray(target, n):
    result = []
    idx = 0
    for i in range(1, n + 1):
        if idx >= len(target):
            break
        result.append("Push")
        if i == target[idx]:
            idx = idx + 1
        else:
            result.append("Pop")
    return result

print(buildArray([1,3], 3))      # ["Push","Push","Pop","Push"]
print(buildArray([1,2,3], 3))    # ["Push","Push","Push"]