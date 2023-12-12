#!/usr/bin/python3
"""
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file.
"""


def minOperations(n):
    """algorthm to find min operations to reach n chars
    1- to access docstrings of the main module (python file) itselt use:
    python3 -c 'print(__import__("test-0-minoperations").minOperations.__doc__)'
    2- to access docstrings a funcion with in a python file or (module) use:
    python3 -c 'print(__import__("test-0-minoperations").minOperations.minOperations.__doc__)'

    """
    copied_all = 0
    total_copied = 1
    op_list = []
    if n <= 1 or not isinstance(n, int):
        return 0
    op_count = 0
    while total_copied < n:
        if n % total_copied == 0:
            op_list.append("copyAll")
            op_list.append("paste")
            op_count += 2
            copied_all = total_copied
            total_copied *= 2
        else:
            op_list.append("paste")
            op_count += 1
            total_copied += copied_all
    print(f"total count= {len(op_list)}")
    print(f"list= {op_list}")

    return op_count

if __name__== "__main__":
  n = 4
  print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
  n = 12
  print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
