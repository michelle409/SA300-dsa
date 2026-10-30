# Problem: Remove Outermost Parentheses
# Pattern: Stack depth counter - skip outermost layer
# Time: O(n) | Space: O(1)

def removeOuterParentheses(s):
    result = ""
    depth = 0
    for i in range(len(s)):
        if s[i] == '(':
            if depth > 0:
                result = result + s[i]
            depth = depth + 1
        else:
            depth = depth - 1
            if depth > 0:
                result = result + s[i]
    return result

print(removeOuterParentheses("(())(())"))        # "()()"
print(removeOuterParentheses("(()())(())"))      # "()()()"
print(removeOuterParentheses("()()"))            # ""