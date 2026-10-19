# Problem: Palindrome Number
# Pattern: Two pointers concept - reverse number mathematically, no string conversion
# Time: O(log n) | Space: O(1)

def isPalindrome(x):
    # negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10

    return original == reversed_num

print(isPalindrome(121))   # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))    # False
print(isPalindrome(0))     # True