def permutations(nums):
  perms = []
  solution = []
  def backtrack():
    if len(nums) == len(solution):
      perms.append(solution[:])
      return
    for num in nums:
      if not num in solution:
        solution.append(num)
        backtrack()
        solution.pop()
  backtrack()
  return perms

if __name__ == "__main__":
  print(permutations([1, 2, 3]))