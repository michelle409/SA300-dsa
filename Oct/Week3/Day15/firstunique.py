# Problem: First Unique Character in a String
# Pattern: Hashmap - count frequencies, find first with count 1
# Time: O(n) | Space: O(1) - only 26 letters

def firstUniqChar(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] = count[s[i]] + 1
        else:
            count[s[i]] = 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))  # 0
print(firstUniqChar("loveleet"))  # 2
print(firstUniqChar("aabb"))      # -1
