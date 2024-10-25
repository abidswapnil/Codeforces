import math

m, n, a = map(int, input().split())

def num_squares(m, n, a):
  mx = math.ceil(m / a)
  ny = math.ceil(n / a)
  
  return max(mx, ny) * min(mx, ny)

print(num_squares(m, n, a))