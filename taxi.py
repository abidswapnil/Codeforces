l = int(input())
g = sorted(map(int, input().strip().split()))

import math

def taxi(l, g):
  ans, prev = 0, 0
  i, j = 0, l - 1
  
  while i <= j:
    if prev and prev + g[i] <= 4:
      prev += g[i]
      i += 1
    else:
      ans += 1
      prev = g[j]
      j -= 1
  
  return ans

print(taxi(l, g))
