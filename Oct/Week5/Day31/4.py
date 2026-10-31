# Problem: Decoded String at Index
# Pattern: Work backwards - find length at each step
# Time: O(n) | Space: O(1)

def decodeAtIndex(s, k):
    length = 0
    for i in range(len(s)):
        if s[i].isdigit():
            length = length * int(s[i])
        else:
            length = length + 1

    for i in range(len(s) - 1, -1, -1):
        k = k % length
        if k == 0 and s[i].isalpha():
            return s[i]
        if s[i].isdigit():
            length = length // int(s[i])
        else:
            length = length - 1

print(decodeAtIndex("leet2code3", 10))  # "o"
print(decodeAtIndex("ha22", 5))          # "h"