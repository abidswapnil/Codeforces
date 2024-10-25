t = int(input().strip())

for _ in range(t):
  size = int(input().strip())
  arr = sorted(map(int, input().strip().split()))
  
  
  def solution(arr):
    ans = (len(arr) - 1) * (max(arr) - min(arr))
    return ans
  
  print(solution(arr))