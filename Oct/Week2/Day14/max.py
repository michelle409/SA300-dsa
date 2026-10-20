# Problem: Maximum Number of Vowels in Substring of Given Length
# Pattern: Fixed sliding window - count vowels in window of size k
# Time: O(n) | Space: O(1)

def maxVowels(s, k):
    vowels = set('aeiou')
    count = 0

    for i in range(k):
        if s[i] in vowels:
            count = count + 1

    max_count = count

    for i in range(k, len(s)):
        if s[i] in vowels:
            count = count + 1
        if s[i - k] in vowels:
            count = count - 1
        if count > max_count:
            max_count = count

    return max_count

print(maxVowels("abciiidef", 3))   # 3
print(maxVowels("aeiou", 2))        # 2
print(maxVowels("leetcode", 3))     # 2