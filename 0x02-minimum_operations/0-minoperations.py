#!/usr/bin/python3
"""
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters
in the file.
"""


def minOperations(n):
    copied_all = 0
    total_copied = 1
    op_list = []
    if n <= 1 or not isinstance(n, int):
        return 0
    op_count = 0
    while total_copied < n:
        if n % total_copied == 0:
            op_list.append("copyAll, past")
            op_count += 2
            copied_all = total_copied
            total_copied *= 2
        else:
            op_list.append("past")
            op_count += 1
            total_copied += copied_all
    return op_count

# Example usage:
# result = minOperations(5)
# print(result)
