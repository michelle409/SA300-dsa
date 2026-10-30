# Problem: Reverse Words in a String
# Pattern: Split, reverse order, rejoin
# Time: O(n) | Space: O(n)
# DON'T use ' '.join(reversed(s.split()))

def reverseWords(s):
    words = s.split()
    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left = left + 1
        right = right - 1
    result = ""
    for i in range(len(words)):
        if i > 0:
            result = result + " "
        result = result + words[i]
    return result

print(reverseWords("the sky is blue"))   # "blue is sky the"
print(reverseWords("  hello world  "))   # "world hello"
print(reverseWords("a good   example"))  # "example good a"