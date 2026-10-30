# Problem: Best Time to Buy and Sell Stock
# Pattern: Single pass - track running min and max profit
# Time: O(n) | Space: O(1)
# DON'T use min() max() inside loop

def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

print(maxProfit([7,1,5,3,6,4]))   # 5
print(maxProfit([7,6,4,3,1]))     # 0