# Problem: Remove K Digits
# Pattern: Monotonic stack - remove larger digits greedily
# Time: O(n) | Space: O(n)

def removeKdigits(num, k):
    stack = []
    for i in range(len(num)):
        while k > 0 and len(stack) > 0 and stack[len(stack)-1] > num[i]:
            stack.pop()
            k = k - 1
        stack.append(num[i])
    while k > 0:
        stack.pop()
        k = k - 1
    result = ""
    leading = True
    for ch in stack:
        if leading and ch == '0':
            continue
        leading = False
        result = result + ch
    return result if result else "0"

print(removeKdigits("1432219", 3))  # "1219"
print(removeKdigits("10200", 1))    # "200"
print(removeKdigits("10", 2))       # "0"