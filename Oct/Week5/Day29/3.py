# Problem: Best Time with Cooldown
# Pattern: State machine - held, sold, rest states
# Time: O(n) | Space: O(1)

def maxProfit(prices):
    held = -prices[0]
    sold = 0
    rest = 0
    for i in range(1, len(prices)):
        prev_held = held
        prev_sold = sold
        prev_rest = rest
        held = max(prev_held, prev_rest - prices[i])
        sold = prev_held + prices[i]
        rest = max(prev_rest, prev_sold)
    return max(sold, rest)

print(maxProfit([1,2,3,0,2]))  # 3
print(maxProfit([1]))           # 0