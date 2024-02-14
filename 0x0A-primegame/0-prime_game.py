#!/usr/bin/python3
""" prime game
  x: number of rounds
  A: array of n integers
"""
def filter_none_zero(value):
  return value != 0

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

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

    for i in range(size):
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
        while True:
          choice = int(input("Marias turn: "))
          if (is_prime(choice)):
            break
      else:
        while True:
          choice = int(input("Bens turn: "))
          if (is_prime(choice)):
            break
      for i in range(len(remaining)):
        if (remaining[i] % choice == 0 and remaining[i] > 1):
          remaining[i] = 0

if maria > ben:
  return ("Maria")
return ("Ben")


if __name__ == "__main__":
    isWinner(5, [2, 5, 1, 4, 3])