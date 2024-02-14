#!/usr/bin/python3
prime = False

def is_prime(n):
  if n == 1:
    return False
  if n == 3:
    return True
  if n == 5:
    return True
  if n%2 == 0 or n%3 == 0:
    return False
  i = 5
  while i <= n:
    if n% i == 0:
      return False

while not prime:
    choice = int(input("Marias turn: "))
    prime = is_prime(choice)
