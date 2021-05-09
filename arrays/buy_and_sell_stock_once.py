"""
Given an array denoting the daily stock price, return the maximum profit that
can be made by buying and then selling one share of that stock. There is no need
to buy if no profit is possible.
"""
def buy_and_sell_stock_once(A):
    max_profit = 0.0
    buy_price = float('inf')
    for cur_price in A:
        max_profit = max(max_profit, cur_price - buy_price)
        buy_price = min(buy_price, cur_price)
    return max_profit

"""
Given an array of integers, find the length of a longest subarray, all of whose
entries are equal.
"""
def length_of_longest_homogeneous_subarray(A):
    ...

