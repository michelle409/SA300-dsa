# Problem: Minimum Remove to Make Valid Parentheses
# Pattern: Stack - track indices of unmatched brackets
# Time: O(n) | Space: O(n)

def minRemoveToMakeValid(s):
    chars = list(s)
    stack = []
    for i in range(len(chars)):
        if chars[i] == '(':
            stack.append(i)
        elif chars[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                chars[i] = ''
    for i in stack:
        chars[i] = ''
    return ''.join(chars)

print(minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
print(minRemoveToMakeValid("a)b(c)d"))         # "ab(c)d"
print(minRemoveToMakeValid("))(("))            # ""