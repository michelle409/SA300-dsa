# Problem: Groups of Special-Equivalent Strings
# Pattern: Signature grouping - sort even and odd indexed chars separately
# Time: O(n*m log m) | Space: O(n)

def numSpecialEquivGroups(words):
    signatures = set()
    for word in words:
        even_chars = []
        odd_chars = []
        for i in range(len(word)):
            if i % 2 == 0:
                even_chars.append(word[i])
            else:
                odd_chars.append(word[i])
        # bubble sort even chars
        n = len(even_chars)
        for x in range(n):
            for y in range(n - 1):
                if even_chars[y] > even_chars[y + 1]:
                    even_chars[y], even_chars[y + 1] = even_chars[y + 1], even_chars[y]
        # bubble sort odd chars
        n = len(odd_chars)
        for x in range(n):
            for y in range(n - 1):
                if odd_chars[y] > odd_chars[y + 1]:
                    odd_chars[y], odd_chars[y + 1] = odd_chars[y + 1], odd_chars[y]
        sig = ''.join(even_chars) + '|' + ''.join(odd_chars)
        signatures.add(sig)
    return len(signatures)

print(numSpecialEquivGroups(["abcd","cdab","cbad","xyzw"]))  # 3
print(numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))  # 3