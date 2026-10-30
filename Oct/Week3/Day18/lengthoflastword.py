# Problem: Length of Last Word
# Pattern: String scan from end - skip trailing spaces, count letters
# Time: O(n) | Space: O(1)

def lengthOfLastWord(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i = i - 1
    count = 0
    while i >= 0 and s[i] != ' ':
        count = count + 1
        i = i - 1
    return count

print(lengthOfLastWord("Hello World"))       # 5
print(lengthOfLastWord("   fly me   to the moon  "))  # 4
print(lengthOfLastWord("luffy is still joyboy"))  # 6