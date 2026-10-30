# Problem: Valid Parentheses
# Pattern: Stack - push open brackets, pop and match on close
# Time: O(n) | Space: O(n)
# DON'T use collections.deque - use plain list as stack

def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for i in range(len(s)):
        if s[i] in '([{':
            stack.append(s[i])
        else:
            if len(stack) == 0 or stack[len(stack)-1] != pairs[s[i]]:
                return False
            stack.pop()
    return len(stack) == 0

print(isValid("()"))      # True
print(isValid("()[]{}")) # True
print(isValid("(]"))      # False
print(isValid("([)]"))    # False
print(isValid("{[]}"))    # True