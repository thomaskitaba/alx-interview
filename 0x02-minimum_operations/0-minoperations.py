#!/usr/bin/python3
""" Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file. """

def minOperations(n):
  copied_all = 0
  total_copied = 1
  op_list = []
  if n <= 1:
    return 0
  op_count = 0
  while total_copied < n:
    if n % total_copied == n:
      op_list.append("copyAll, past")
      op_count += 2
      copied_all = 1
      # total_copied += copied_all
      total_copied = 2*copied_all
    elif n % total_copied == 0:
      op_list.append("copyAll, past")
      op_count += 2
      copied_all = total_copied
      total_copied = 2 * copied_all

    elif n % total_copied != 0:
      op_list.append("past")
      op_count += 1
      total_copied += copied_all
    else:
      return (0)
  return (op_count)
