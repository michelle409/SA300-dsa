# Problem: Find the Difference
# Pattern: XOR - XOR all chars from both strings, extra char remains
# Time: O(n) | Space: O(1)

def findTheDifference(s, t):
    result = 0
    for i in range(len(s)):
        result = result ^ ord(s[i])
    for i in range(len(t)):
        result = result ^ ord(t[i])
    return chr(result)

print(findTheDifference("abcd", "abcde"))  # e
print(findTheDifference("", "y"))          # y