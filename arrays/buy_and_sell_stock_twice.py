"""
Given an array of stock prices, compute the maximum profit that can be made by
buying and selling a share at most twice.
"""
def buy_and_sell_stock_twice(prices):
    max_total_profit = 0
    min_price_so_far = float('inf')
    first_buy_sell_profits = [0] * len(prices)

    # find first buy/sell profit going forwards
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # find second buy/sell profit going backwards
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit,
                               max_price_so_far - price + first_buy_sell_profits[i-1])

    return max_total_profit

A = [12,11,13,9,12,8,14,13,15]
buy_and_sell_stock_twice(A)

"""
Solve the same problem in O(n) time and O(1) space.
"""
def buy_and_sell_stock_twice_v2(A):
    """
    buy1 is minimum price so far.
    sell1 is maximum profit so far if you sell the stock.
    buy2 is the maximum profit so far if you buy the stock again.
    sell2 is final profit.

    The situation in which it keeps increasing doesn't matter.
    However if the slope changes from increasing to decreasing, sell1 will stay
    the same while buy2 will get updated to the local minimum.
    """
    buy1 = float('inf')
    buy2 = float('inf')
    sell1 = 0
    sell2 = 0

    for price in A:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        buy2 = min(buy2, price - sell1)
        sell2 = max(sell2, price - buy2)

    return sell2


