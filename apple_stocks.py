#failed the first attempt

stock_prices = [100, 17, 6, 5, 4, 3, 2]

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