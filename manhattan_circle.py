
t = int(input())
for _ in range(t):
  n, m = [int(x) for x in input().strip().split()]
  mat = []
  ans = []
  
  for _ in range(n):
    mat.append(list(input().strip()))
  
  for i in range(n):
    for j in range(m):
      if mat[i][j] == '#':
        ans.append([ i +1, j+ 1])
  
  print(*ans[len(ans) // 2])