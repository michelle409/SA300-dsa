# Problem: Isomorphic Strings
# Pattern: Bijective hashmap - map both directions simultaneously
# Time: O(n) | Space: O(1) - only 256 ASCII chars
# DON'T use len(set(zip(s,t))) == len(set(s)) == len(set(t))

def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        if sc in s_to_t:
            if s_to_t[sc] != tc:
                return False
        else:
            s_to_t[sc] = tc
        if tc in t_to_s:
            if t_to_s[tc] != sc:
                return False
        else:
            t_to_s[tc] = sc
    return True

print(isIsomorphic("egg", "add"))    # True
print(isIsomorphic("foo", "bar"))    # False
print(isIsomorphic("paper", "title"))  # True