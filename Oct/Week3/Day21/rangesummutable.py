# Problem: Range Sum Query - Mutable
# Pattern: Prefix sum rebuild on update (simplified version)
# Time: O(n) update, O(1) query | Space: O(n)
# Note: optimal uses segment tree but prefix rebuild is acceptable here

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def update(self, index, val):
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.prefix[i + 1] = self.prefix[i] + self.nums[i]

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]