# Problem: Find All Anagrams in a String
# Pattern: Fixed sliding window + hashmap frequency matching
# Time: O(n) | Space: O(1) - only 26 letters

def findAnagrams(s, p):
    result = []

    if len(p) > len(s):
        return result

    p_count = {}
    window_count = {}

    for i in range(len(p)):
        if p[i] in p_count:
            p_count[p[i]] = p_count[p[i]] + 1
        else:
            p_count[p[i]] = 1
        if s[i] in window_count:
            window_count[s[i]] = window_count[s[i]] + 1
        else:
            window_count[s[i]] = 1

    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # add new right character
        if s[i] in window_count:
            window_count[s[i]] = window_count[s[i]] + 1
        else:
            window_count[s[i]] = 1

        # remove old left character
        left_char = s[i - len(p)]
        window_count[left_char] = window_count[left_char] - 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result

print(findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(findAnagrams("abab", "ab"))          # [0, 1, 2]