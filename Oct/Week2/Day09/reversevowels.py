# Problem: Reverse Vowels of a String
# Pattern: Two pointers - skip non-vowels, swap only vowels
# Time: O(n) | Space: O(n) - need list since strings immutable

def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        while left < right and chars[left] not in vowels:
            left = left + 1
        while left < right and chars[right] not in vowels:
            right = right - 1
        chars[left], chars[right] = chars[right], chars[left]
        left = left + 1
        right = right - 1

    return ''.join(chars)

print(reverseVowels("IceCreAm"))  # AceCreIm
print(reverseVowels("leetcode"))  # leotcede