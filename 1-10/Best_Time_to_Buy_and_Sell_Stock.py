# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# def best_time_to_buy_best_time_to_sell(prices):
#     maximum = 0 
#     for i in range(0, len(prices)):
#         value = prices[i]
#         for j in range(1+i, len(prices)):
#             if prices[j] - value > maximum:
#                 maximum = prices[j] - value
#     return print(maximum)
# best_time_to_buy_best_time_to_sell(prices)


prices = [7,1,5,3,6,4]

def maxProfit(prices):
    minprice = prices[0]
    maxProfit = 0
    for price in prices:
        if price > minprice and price - minprice > maxProfit:     
            maxProfit = price - minprice
        elif price < minprice: 
            minprice = price
    return print(maxProfit)

maxProfit(prices)