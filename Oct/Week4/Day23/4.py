# Problem: Remove All Adjacent Duplicates In String
# Pattern: Stack - pop when top equals current
# Time: O(n) | Space: O(n)

def removeDuplicates(s):
    stack = []
    for i in range(len(s)):
        if len(stack) > 0 and stack[len(stack)-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)

print(removeDuplicates("abbaca"))  # "ca"
print(removeDuplicates("azxxzy"))  # "ay"