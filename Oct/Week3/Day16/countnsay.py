# Problem: Count and Say
# Pattern: String simulation - read and encode previous term
# Time: O(n * m) | Space: O(m)

def countAndSay(n):
    result = "1"
    for i in range(1, n):
        current = ""
        count = 1
        for j in range(1, len(result)):
            if result[j] == result[j - 1]:
                count = count + 1
            else:
                current = current + str(count) + result[j - 1]
                count = 1
        current = current + str(count) + result[len(result) - 1]
        result = current
    return result

print(countAndSay(1))  # "1"
print(countAndSay(4))  # "1211"
print(countAndSay(5))  # "111221"