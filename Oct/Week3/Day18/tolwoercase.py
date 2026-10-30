# Problem: To Lower Case
# Pattern: String scan - convert uppercase to lowercase manually
# Time: O(n) | Space: O(n)
# DON'T use s.lower()

def toLowerCase(s):
    result = ""
    for i in range(len(s)):
        ch = s[i]
        if ord(ch) >= 65 and ord(ch) <= 90:
            result = result + chr(ord(ch) + 32)
        else:
            result = result + ch
    return result

print(toLowerCase("Hello"))    # "hello"
print(toLowerCase("here"))     # "here"
print(toLowerCase("LOVELY"))   # "lovely"