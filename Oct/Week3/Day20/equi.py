# Problem: Equilibrium Point
# Pattern: Same pivot logic - 1-indexed return
# Time: O(n) | Space: O(1)

def equilibriumPoint(arr, n):
    total = 0
    for i in range(n):
        total = total + arr[i]
    left_sum = 0
    for i in range(n):
        right_sum = total - left_sum - arr[i]
        if left_sum == right_sum:
            return i + 1
        left_sum = left_sum + arr[i]
    return -1

print(equilibriumPoint([1,3,5,2,2], 5))  # 3
print(equilibriumPoint([1,2,3], 3))       # -1