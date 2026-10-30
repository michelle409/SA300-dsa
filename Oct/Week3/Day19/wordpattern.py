# Problem: Word Pattern
# Pattern: Bijective hashmap - same as isomorphic but word level
# Time: O(n) | Space: O(n)

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    p_to_w = {}
    w_to_p = {}
    for i in range(len(pattern)):
        p = pattern[i]
        w = words[i]
        if p in p_to_w:
            if p_to_w[p] != w:
                return False
        else:
            p_to_w[p] = w
        if w in w_to_p:
            if w_to_p[w] != p:
                return False
        else:
            w_to_p[w] = p
    return True

print(wordPattern("abba", "dog cat cat dog"))  # True
print(wordPattern("abba", "dog cat cat fish")) # False
print(wordPattern("aaaa", "dog cat cat dog"))  # False