# Problem: Check If Word Occurs As Prefix
# Pattern: String scanning - check prefix match word by word
# Time: O(n*m) | Space: O(1)

def isPrefixOfWord(sentence, searchWord):
    words = sentence.split(" ")
    for i in range(len(words)):
        word = words[i]
        if len(searchWord) <= len(word):
            match = True
            for j in range(len(searchWord)):
                if searchWord[j] != word[j]:
                    match = False
                    break
            if match:
                return i + 1
    return -1

print(isPrefixOfWord("i love eating burger", "burg"))  # 4
print(isPrefixOfWord("this problem is an easy problem", "pro"))  # 2
print(isPrefixOfWord("i am tired", "you"))  # -1