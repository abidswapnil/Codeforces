t = int(input())
for _ in range(t):
  n = int(input())
  
  ans = None
  maxDiv = float('-inf')
  minRem = float('inf')
  for i in range(2, n + 1):
    if n // i >= maxDiv and n % i <= minRem:
      maxDiv = n // i
      minRem = n % i
      ans = i
  print(ans)