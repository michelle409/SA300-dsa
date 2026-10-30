# Problem: Make The String Great
# Pattern: Stack - collapse adjacent same-letter different-case pairs
# Time: O(n) | Space: O(n)

def makeGood(s):
    stack = []
    for i in range(len(s)):
        if (len(stack) > 0 and
            stack[len(stack)-1] != s[i] and
            stack[len(stack)-1].lower() == s[i].lower()):
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)

print(makeGood("leEeetcode"))  # "leetcode"
print(makeGood("abBAcC"))      # ""
print(makeGood("s"))           # "s"