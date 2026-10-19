# Problem: Reverse Only Letters
# Pattern: Two pointers - skip non-letters, swap only letters
# Time: O(n) | Space: O(n) - strings are immutable in Python so need a list

def reverseOnlyLetters(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        while left < right and not chars[left].isalpha():
            left = left + 1
        while left < right and not chars[right].isalpha():
            right = right - 1
        chars[left], chars[right] = chars[right], chars[left]
        left = left + 1
        right = right - 1

    return ''.join(chars)

print(reverseOnlyLetters("ab-cd"))              # "dc-ba"
print(reverseOnlyLetters("a-bC-dEf-ghIj"))     # "j-Ih-gfE-dCba"
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"