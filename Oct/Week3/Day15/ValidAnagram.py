# Problem: Valid Anagram
# Pattern: Hashmap frequency count - compare character counts of both strings
# Time: O(n) | Space: O(1) - only 26 letters
# DON'T use Counter or sorted()

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] = count[s[i]] + 1
        else:
            count[s[i]] = 1

    for i in range(len(t)):
        if t[i] not in count or count[t[i]] == 0:
            return False
        count[t[i]] = count[t[i]] - 1

    return True

print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))           # False