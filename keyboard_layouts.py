from collections import defaultdict

dic = defaultdict()

s = input()
t = input()
u = input()

for i, z in zip(s, t):
	dic[i] = z

res = ''

for l in u:
	if l.lower() in dic:
		new = dic[l.lower()]
		if l.islower():
			res += new
		else:
			res += new.upper()
	else:
		res += l

print(res)