# Problem: Valid Palindrome
# Pattern: Two pointers from both ends - skip non-alphanumeric inline
# Time: O(n) | Space: O(1)
# DON'T use s == s[::-1] or ''.join() cleanup - do it inline

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # skip non-alphanumeric on left
        while left < right and not s[left].isalnum():
            left = left + 1
        # skip non-alphanumeric on right
        while left < right and not s[right].isalnum():
            right = right - 1

        if s[left].lower() != s[right].lower():
            return False

        left = left + 1
        right = right - 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                       # False
print(isPalindrome(" "))                                # True