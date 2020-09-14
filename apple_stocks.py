#failed the first attempt
'''objective is to find the maximum profit that can be obtained by buying and selling a stock. list contains prices of stocks throughout
the day and the index is the time since market opening. No short selling allowed or if prices continue to go down, return mininum loss - 
used greedy algorithm. '''

stock_prices = [10, 7, 6, 5, 4, 3, 20]
wrong_prices = [1,2,3]

def get_max_profit(stock_prices):

   max_profit = stock_prices[1] - stock_prices[0]
   min_price = stock_prices[0]
    
   for i in range(1, len(stock_prices)):
     current_price = stock_prices[i]

     potential_profit = current_price - min_price

     max_profit = max(max_profit, potential_profit)

     min_price = min(min_price, current_price)

   return max_profit
   
print(get_max_profit(stock_prices))
