# Problem: Baseball Game
# Pattern: Stack as running state - simulate operations
# Time: O(n) | Space: O(n)
# DON'T use collections.deque - plain list is your stack

def calPoints(operations):
    stack = []
    for i in range(len(operations)):
        op = operations[i]
        if op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(stack[len(stack)-1] * 2)
        elif op == '+':
            stack.append(stack[len(stack)-1] + stack[len(stack)-2])
        else:
            stack.append(int(op))
    total = 0
    for i in range(len(stack)):
        total = total + stack[i]
    return total

print(calPoints(["5","2","C","D","+"]))    # 30
print(calPoints(["5","-2","4","C","D","9","+","+"]))  # 27