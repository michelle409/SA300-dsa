# Problem: Find and Replace Pattern
# Pattern: Bijective hashmap - check each word against pattern
# Time: O(n*m) | Space: O(1)

def findAndReplacePattern(words, pattern):
    def matches(word, pattern):
        if len(word) != len(pattern):
            return False
        w_to_p = {}
        p_to_w = {}
        for i in range(len(word)):
            w = word[i]
            p = pattern[i]
            if w in w_to_p:
                if w_to_p[w] != p:
                    return False
            else:
                w_to_p[w] = p
            if p in p_to_w:
                if p_to_w[p] != w:
                    return False
            else:
                p_to_w[p] = w
        return True

    result = []
    for i in range(len(words)):
        if matches(words[i], pattern):
            result.append(words[i])
    return result

print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
# ["mee","aqq"]