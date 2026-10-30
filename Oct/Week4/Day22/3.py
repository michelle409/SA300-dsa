# Problem: Score of Parentheses
# Pattern: Stack - track running score at each depth level
# Time: O(n) | Space: O(n)

def scoreOfParentheses(s):
    stack = [0]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(0)
        else:
            val = stack.pop()
            if val == 0:
                stack[len(stack)-1] = stack[len(stack)-1] + 1
            else:
                stack[len(stack)-1] = stack[len(stack)-1] + 2 * val
    return stack[0]

print(scoreOfParentheses("()"))      # 1
print(scoreOfParentheses("(())"))    # 2
print(scoreOfParentheses("()()"))    # 2
print(scoreOfParentheses("((()))"))  # 4