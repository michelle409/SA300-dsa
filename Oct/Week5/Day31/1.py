# Problem: Backspace String Compare
# Pattern: Stack simulation - process backspace then compare
# Time: O(n+m) | Space: O(n+m)
# DON'T use collections.deque

def backspaceCompare(s, t):
    def process(string):
        stack = []
        for i in range(len(string)):
            if string[i] != '#':
                stack.append(string[i])
            elif len(stack) > 0:
                stack.pop()
        return ''.join(stack)

    return process(s) == process(t)

print(backspaceCompare("ab#c", "ad#c"))   # True
print(backspaceCompare("ab##", "c#d#"))   # True
print(backspaceCompare("a#c", "b"))       # False