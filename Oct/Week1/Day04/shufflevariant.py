# Problem: Shuffle the Array
# Pattern: Index arithmetic - interleave first and second half
# Time: O(n) | Space: O(n)

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

print(shuffle([2,5,1,3,4,7], 3))        # [2,3,5,4,1,7]
print(shuffle([1,2,3,4,4,3,2,1], 4))    # [1,4,2,3,3,2,4,1]
print(shuffle([1,1,2,2], 2))            # [1,2,1,2]