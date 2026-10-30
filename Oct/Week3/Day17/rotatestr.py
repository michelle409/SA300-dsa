# Problem: Rotate String
# Pattern: String simulation - check if s+s contains goal
# Time: O(n^2) | Space: O(n)

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    doubled = s + s
    n = len(goal)
    for i in range(len(doubled) - n + 1):
        match = True
        for j in range(n):
            if doubled[i + j] != goal[j]:
                match = False
                break
        if match:
            return True
    return False

print(rotateString("abcde", "cdeab"))  # True
print(rotateString("abcde", "abced"))  # False