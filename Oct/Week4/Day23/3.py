# Problem: Final Prices With Special Discount
# Pattern: Monotonic stack - next smaller or equal element
# Time: O(n) | Space: O(n)

def finalPrices(prices):
    stack = []
    result = list(prices)
    for i in range(len(prices)):
        while len(stack) > 0 and prices[stack[len(stack)-1]] >= prices[i]:
            idx = stack.pop()
            result[idx] = prices[idx] - prices[i]
        stack.append(i)
    return result

print(finalPrices([8,4,6,2,3]))   # [4,2,4,2,3]
print(finalPrices([1,2,3,4,5]))   # [1,2,3,4,5]
print(finalPrices([10,1,1,6]))    # [9,0,1,6]