#!/usr/bin/python3
""" prime game
  x: number of rounds
  A: array of n integers
"""


def isWinner(x, nums):
  """ find winner for each round """
  ben = 0
  maria = 0
  remaining = nums
  mariasChoice = input("Maria's Turn:")
  bensChoice = input("Ben's Turn:")
  gameOver = False
  for round in range(x):
    if gameOver:
      break
    for j in range(len(remaining) - 1):
      if len(remaining) == 0:
          gameOver = True
          break
      if j % 2 == 0:
        Choice = input("Maria's Turn:")
      else:
        Choice = input("Ben's Turn:")

      if remaining[j] % int(Choice) == 0:
        remaining.pop(j)
        print(remaining)
        if j > 0 and j % 2 != 0:
            ben += 1
        else:
            maria + 1
  return (f"{mariasChoice}  {bensChoice}  {remaining}")
  if ben > maria:
    return "Ben"
  return "Maria"

if __name__ == "__main__":
    isWinner(5, [2, 5, 1, 4, 3])