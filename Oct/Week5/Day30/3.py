# Problem: Rotate Array
# Pattern: Three reversal trick
# Time: O(n) | Space: O(1)

def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

nums1 = [1,2,3,4,5,6,7]
rotate(nums1, 3)
print(nums1)  # [5,6,7,1,2,3,4]