# Problem: Validate Stack Sequences
# Pattern: Stack simulation - simulate push/pop sequence
# Time: O(n) | Space: O(n)

def validateStackSequences(pushed, popped):
    stack = []
    j = 0
    for i in range(len(pushed)):
        stack.append(pushed[i])
        while len(stack) > 0 and stack[len(stack)-1] == popped[j]:
            stack.pop()
            j = j + 1
    return len(stack) == 0

print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))  # True
print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))  # False