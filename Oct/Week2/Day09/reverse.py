# Problem: Reverse String
# Pattern: Two pointers - swap from both ends moving inward
# Time: O(n) | Space: O(1) - in-place
# DON'T use s.reverse(), reversed(s), or s[::-1]

def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1

s1 = ["h","e","l","l","o"]
reverseString(s1)
print(s1)  # ["o","l","l","e","h"]

s2 = ["H","a","n","n","a","h"]
reverseString(s2)
print(s2)  # ["h","a","n","n","a","H"]