#!/usr/bin/python3
""" Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file. """

def minOperations(n):
  opCount = 2
  mid = 0
  hCount = 0
  remaining = 0
  allText = "H"

  if n == 1:
    return 0
  if n == 2:
    return 1
  if n == 3:
    return 3
  if n == 4:
    return 4

  if n > 4:
    mid = int(n / 2)
    remaining = n % 2
    # opCount += 2
    # while len(allText[-1:] == n):
    while hCount <= mid:
      if mid % opCount == 0:
        opCount += 2  # for copy
        allText = f"{allText} + {allText}"
        hCount = len(allText)
      else:
        opCount += 1
      if mid == hCount:
        return opCount




  return (f"mid: {mid}  op: {opCount}")