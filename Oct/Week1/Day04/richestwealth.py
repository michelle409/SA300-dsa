# Problem: Richest Customer Wealth
# Pattern: 2D array - sum each row, track maximum
# Time: O(m*n) | Space: O(1)

def maximumWealth(accounts):
    max_wealth = 0
    for i in range(len(accounts)):
        wealth = 0
        for j in range(len(accounts[i])):
            wealth = wealth + accounts[i][j]
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

print(maximumWealth([[1,2,3],[3,2,1]]))          # 6
print(maximumWealth([[1,5],[7,3],[3,5]]))         # 10
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))  # 17