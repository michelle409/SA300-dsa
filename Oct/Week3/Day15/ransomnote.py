# Problem: Ransom Note
# Pattern: Hashmap - count magazine letters, check if ransomNote can be built
# Time: O(n) | Space: O(1) - only 26 letters

def canConstruct(ransomNote, magazine):
    count = {}
    for i in range(len(magazine)):
        if magazine[i] in count:
            count[magazine[i]] = count[magazine[i]] + 1
        else:
            count[magazine[i]] = 1
    for i in range(len(ransomNote)):
        if ransomNote[i] not in count or count[ransomNote[i]] == 0:
            return False
        count[ransomNote[i]] = count[ransomNote[i]] - 1
    return True

print(canConstruct("a", "b"))     # False
print(canConstruct("aa", "ab"))   # False
print(canConstruct("aa", "aab"))  # True