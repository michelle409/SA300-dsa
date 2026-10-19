# Problem: Reverse String II
# Pattern: Two pointers - reverse first k chars every 2k chunk
# Time: O(n) | Space: O(n) - strings immutable in Python so need list

def reverseStr(s, k):
    chars = list(s)
    i = 0
    while i < len(chars):
        left = i
        right = i + k - 1
        if right >= len(chars):
            right = len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left = left + 1
            right = right - 1
        i = i + 2 * k
    return ''.join(chars)

print(reverseStr("abcdefg", 2))  # bacdfeg
print(reverseStr("abcd", 2))     # bacd