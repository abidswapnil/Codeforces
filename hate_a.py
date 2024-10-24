t = input()

def hateA(t):
	res = ''
	for i in range(len(t)):
		if t[i] != 'a': res += t[i]
		if res == t[i + 1:]: return t[:i + 1]

	return ':('

print(hateA(t))