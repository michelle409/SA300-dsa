# Problem: String Compression
# Pattern: Two pointers read-write - compress in place
# Time: O(n) | Space: O(1)

def compress(chars):
    write = 0
    read = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read = read + 1
            count = count + 1
        chars[write] = char
        write = write + 1
        if count > 1:
            count_str = str(count)
            for c in count_str:
                chars[write] = c
                write = write + 1
    return write

chars1 = ["a","a","b","b","c","c","c"]
print(compress(chars1))   # 6
print(chars1[:6])          # ["a","2","b","2","c","3"]

chars2 = ["a"]
print(compress(chars2))   # 1