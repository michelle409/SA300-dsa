# Problem: Reverse Prefix of Word
# Pattern: Two pointers - find first occurrence of ch, reverse prefix
# Time: O(n) | Space: O(n) - need list since strings immutable

def reversePrefix(word, ch):
    chars = list(word)
    end = -1

    for i in range(len(chars)):
        if chars[i] == ch:
            end = i
            break

    if end == -1:
        return word

    left = 0
    right = end
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left = left + 1
        right = right - 1

    return ''.join(chars)

print(reversePrefix("abcdefd", "d"))  # dcbaefd
print(reversePrefix("xyxzxe", "z"))   # zxyxxe
print(reversePrefix("abcd", "z"))     # abcd