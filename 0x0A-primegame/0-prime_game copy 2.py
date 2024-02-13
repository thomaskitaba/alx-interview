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
  gameOver = False
  tempRemaining = []

  for turn in range(len(remaining)):
    if turn == 0:
      choice = int(input("Marias turn: "))
    else:
      choice = int(input("Ben turn: "))
    # print(f":before pop {remaining}")
    tempRemaining = remianing
    tempRemaining = remaining
    for num, index in enumerate(tempRemaining):
      if num % choice == 0:

        print(f"poped {num}")
        remaining.pop(Remaining[index])
        print(f":after pop {remaining}")
        if turn % 2 == 0:
          maria += 1
        else:
          ben += 1

#   return (f"{mariasChoice}  {bensChoice}  {remaining}")
  if ben > maria:
    return "Ben"
  return "Maria"

if __name__ == "__main__":
    isWinner(5, [2, 5, 1, 4, 3])