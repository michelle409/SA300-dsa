# Problem: Decompress Run-Length Encoded List
# Pattern: Walk pairs, repeat value freq times
# Time: O(n) | Space: O(n)

def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i + 1]
        for j in range(freq):
            result.append(val)
    return result

print(decompressRLElist([1,2,3,4]))   # [2,4,4,4]
print(decompressRLElist([1,1,2,3]))   # [1,3,3]