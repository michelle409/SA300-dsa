# Problem: Find Common Characters
# Pattern: Frequency dict - minimum count across all words
# Time: O(n*m) | Space: O(1) - only 26 letters

def commonChars(words):
    min_freq = {}
    for ch in words[0]:
        min_freq[ch] = min_freq.get(ch, 0) + 1

    for i in range(1, len(words)):
        word_freq = {}
        for ch in words[i]:
            word_freq[ch] = word_freq.get(ch, 0) + 1
        for ch in min_freq:
            if ch in word_freq:
                if word_freq[ch] < min_freq[ch]:
                    min_freq[ch] = word_freq[ch]
            else:
                min_freq[ch] = 0

    result = []
    for ch in min_freq:
        for j in range(min_freq[ch]):
            result.append(ch)
    return result

print(commonChars(["bella","label","roller"]))  # ["e","l","l"]
print(commonChars(["cool","lock","cook"]))       # ["c","o"]