def t(n):
	return set([int(i * (i +1) / 2) for i in range(n)])
	
def p(n):
	return set([int(i*(3*i-1)/2) for i in range(n)])

def h(n):
	return set([int(i*(2*i-1)) for i in range(n)])
	
def main():
	n = 100000
	tr = t(n)
	pe = p(n)
	he = h(n)
	
	print(set.intersection(tr, pe, he))
	
main()

# 1533776805
# Completed on Tue, 16 Mar 2021, 17:03