# Problem: Reverse Words in a String III
# Pattern: Two pointers - find word boundaries, reverse each word in place
# Time: O(n) | Space: O(n) - strings immutable in Python
# DON'T use ' '.join(w[::-1] for w in s.split())

def reverseWords(s):
    chars = list(s)
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == ' ':
            left = start
            right = i - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left = left + 1
                right = right - 1
            start = i + 1
    return ''.join(chars)

print(reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
print(reverseWords("Mr Ding"))                       # "rM gniD"