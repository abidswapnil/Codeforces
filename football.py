position = input()

def is_dangerous(pos):
  prev = pos[0]
  count = 1
  mx_count = count
  
  for i in range(1, len(pos)):
    if pos[i] == prev:
      count += 1
    else:
      count = 1
    prev = pos[i]
    mx_count = max(mx_count, count)
  
  return 'YES' if mx_count >= 7 else 'NO'


print(is_dangerous(position))