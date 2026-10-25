# Problem: Group Anagrams
# Pattern: Hashmap - sort each word as key, group same keys together
# Time: O(n * k) where k is max word length | Space: O(n)
# Use bubble sort instead of sorted()

def groupAnagrams(strs):
    groups = {}

    for i in range(len(strs)):
        chars = list(strs[i])
        n = len(chars)
        for x in range(n):
            for y in range(n - 1):
                if chars[y] > chars[y + 1]:
                    chars[y], chars[y + 1] = chars[y + 1], chars[y]
        key = ''.join(chars)

        if key in groups:
            groups[key].append(strs[i])
        else:
            groups[key] = [strs[i]]

    result = []
    for key in groups:
        result.append(groups[key])
    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams([""]))   # [[""]]
print(groupAnagrams(["a"]))  # [["a"]]