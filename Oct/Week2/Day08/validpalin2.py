# Problem: Valid Palindrome II
# Pattern: Two pointers - on mismatch try skipping left or right once
# Time: O(n) | Space: O(1)

def validPalindrome(s):
    def isPalin(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # try skipping left OR skipping right
            return isPalin(s, left + 1, right) or isPalin(s, left, right - 1)
        left = left + 1
        right = right - 1

    return True

print(validPalindrome("aba"))   # True
print(validPalindrome("abca"))  # True
print(validPalindrome("abc"))   # False