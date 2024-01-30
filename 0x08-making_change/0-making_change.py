#!/usr/bin/python3
"""
  Given a pile of coins of different values,
  determine the fewest number of coins needed
  to meet a given amount total.
"""


def makeChange(coins, total):
    """
      coins: list of values of the coins in our possession
      total: the change amount in question
    """
    if total <= 0:
        return 0
    count = 0
    tempTotal = total
    coinList = sorted(coins, reverse=True)
    for coin in coinList:
        while (tempTotal >= coin):
            count += 1
            tempTotal = tempTotal - coin
    if tempTotal == 0:
        return count
    return -1
