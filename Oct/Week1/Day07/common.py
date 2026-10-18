# Problem: Find Common Characters
# Pattern: Hashmap frequency - take minimum count across all words
# Time: O(n*m) | Space: O(1) - only 26 letters

def commonChars(words):
    # build freq dict for first word
    min_freq = {}
    for ch in words[0]:
        if ch in min_freq:
            min_freq[ch] = min_freq[ch] + 1
        else:
            min_freq[ch] = 1

    # for each remaining word, keep minimum count
    for i in range(1, len(words)):
        word_freq = {}
        for ch in words[i]:
            if ch in word_freq:
                word_freq[ch] = word_freq[ch] + 1
            else:
                word_freq[ch] = 1
        # update min_freq to keep minimums
        for ch in min_freq:
            if ch in word_freq:
                if word_freq[ch] < min_freq[ch]:
                    min_freq[ch] = word_freq[ch]
            else:
                min_freq[ch] = 0

    # build result from min frequencies
    result = []
    for ch in min_freq:
        for count in range(min_freq[ch]):
            result.append(ch)

    return result

print(commonChars(["bella","label","roller"]))  # ["e","l","l"]
print(commonChars(["cool","lock","cook"]))       # ["c","o"]