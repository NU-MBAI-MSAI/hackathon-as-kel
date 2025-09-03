'''Authors: Sneha Basu, Anisha Salunkhe'''

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    curr_low = prices[0] #3
    max_profit = 0
    for price in prices:
        if price < curr_low:
            curr_low = price
        max_profit = max(max_profit,  price - curr_low) #0, 7,
    return max_profit

if __name__ == '__main__':
    print(maxProfit([0,0,0,0,0]) == 0 )
    print(maxProfit([1,2,3,4,5]) == 4)
    print(maxProfit([1]) == 0)
    print(maxProfit([7,1,3,4,8,5]) == 7)
    print(maxProfit([]) == 0)
    print(maxProfit([10,3,1,5]) == 4)