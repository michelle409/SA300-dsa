# Problem: Range Sum Query Immutable
# Pattern: Prefix sum - build once, query in O(1)
# Time: O(n) build, O(1) query | Space: O(n)

class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))   # 1
print(obj.sumRange(2, 5))   # -1
print(obj.sumRange(0, 5))   # -3