#| Given a array of numbers representing the stock prices of a company in chronological order,
#| write a function that calculates the maximum profit you could have made from buying and
#| selling that stock once. You must buy before you can sell it.

#-----------------#
# Define Function #
#-----------------#

def max_profit(prices):
    #| Initialise min_price to the first price in the list and max_profit to 0.
    if not prices:  # Check if the prices list is empty
        return 0
    min_price = prices[0]
    max_profit = 0

    #| Iterate through the list of prices, starting from the second price
    for price in prices[1:]:
        #| Calculate the profit by subtracting the min_price seen so far from the current price
        profit = price - min_price
        
        #| Update the max_profit if the calculated profit is greater than the current max_profit
        max_profit = max(max_profit, profit)
        
        #| Update the min_price if the current price is less than the min_price seen so far
        min_price = min(min_price, price)
        
    return max_profit

#------------------#
# Test Application #
#------------------#

prices = [9, 11, 8, 5, 7, 10]
print(max_profit(prices))  # Output: 5
