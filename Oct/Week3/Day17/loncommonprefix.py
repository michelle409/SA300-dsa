# Problem: Longest Common Prefix
# Pattern: Vertical scan - compare same position across all strings
# Time: O(n*m) | Space: O(1)
# DON'T use os.path.commonprefix() or zip(*strs)

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(longestCommonPrefix(["dog","racecar","car"]))      # ""
print(longestCommonPrefix(["a"]))                        # "a"