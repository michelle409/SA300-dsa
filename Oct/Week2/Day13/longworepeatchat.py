# Problem: Longest Substring Without Repeating Characters
# Pattern: Variable sliding window + hashmap - shrink when duplicate found
# Time: O(n) | Space: O(n)

def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))      # 1
print(lengthOfLongestSubstring("pwwkew"))     # 3