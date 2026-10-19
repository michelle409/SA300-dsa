# Problem: Palindromic Substrings
# Pattern: Expand around center - odd and even length palindromes
# Time: O(n^2) | Space: O(1)

def countSubstrings(s):
    count = 0

    def expand(left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result = result + 1
            left = left - 1
            right = right + 1
        return result

    for i in range(len(s)):
        count = count + expand(i, i)      # odd length - single char center
        count = count + expand(i, i + 1)  # even length - two char center

    return count

print(countSubstrings("abc"))  # 3
print(countSubstrings("aaa"))  # 6