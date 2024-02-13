#!/usr/bin/python3
""" prime game
  x: number of rounds
  A: array of n integers
"""
def filter_none_zero(value):
  return value != 0

def isWinner(x, nums):
  """ find winner for each round """
  ben = 0
  maria = 0
  remaining = nums
  gameOver = False
  tempRemaining = remaining
  size = len(nums)
  winner = ''
  for turn in range(x):

    for turn in range(size):
      # tempRemaining = list(value for value in remaining if value != 0)
      print(remaining)
      tempRemaining = list (filter(filter_none_zero, remaining))
      if (len(tempRemaining) <= 1):
        print(tempRemaining)
        if turn == 0:
          # print(f"winner ben")
          ben += 1
        else:
          maria += 1
          # print(f"winner maria")
        break
      print(tempRemaining)
      if turn % 2 == 0 :
        choice = int(input("Marias turn: "))

      else:
        choice = int(input("Ben turn: "))
      for i in range(len(remaining)):
        if (remaining[i] % choice == 0 and remaining[i] > 1):
          remaining[i] = 0

    if maria > ben:
      return ("Maria")
    return ("Ben")


if __name__ == "__main__":
    isWinner(5, [2, 5, 1, 4, 3])