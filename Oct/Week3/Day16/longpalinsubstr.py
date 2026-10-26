# Problem: Longest Palindromic Substring
# Pattern: Expand around center - check odd and even length palindromes
# Time: O(n^2) | Space: O(1)
# DON'T use s == s[::-1] or dynamic programming

def longestPalindrome(s):
    result = ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left + 1:right]

    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even

    return result

print(longestPalindrome("babad"))   # "bab"
print(longestPalindrome("cbbd"))    # "bb"
print(longestPalindrome("a"))       # "a"