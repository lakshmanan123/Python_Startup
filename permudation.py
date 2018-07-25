s = "lax"
def fact(number):
	if number == 1:
		return 1
	return number * fact(number - 1 )

def main():
	limit = fact(len(s))
	st = list(s)
	ith = 0
	jth = 1
	l = len(st)
	for i in range(0,limit):
		if l == ith :
			ith = 0
		if l == jth :
			jth = 0
		print("".join(st))
		st[ith],st[jth] = st[jth],st[ith]
		ith += 1
		jth += 1

if __name__ == "__main__":
	main()