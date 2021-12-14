from math import isqrt

def prime(n):
	if n == 1:
		return False
	for i in range(2, isqrt(n)+1):
		if n % i == 0:
			return False
	return True
	
def trunc(n):
	s = str(n)
	for n in range(len(s)-1, 0, -1):
		a = prime(int(s[:n]))
		b = prime(int(s[n:]))
		if a and b:
			continue
		else:
			return False
	else:
		return True
		
def main():
	trunc_primes = []
	n = 8
	while len(trunc_primes) < 100001 and n < 1000000:
		if prime(n) and trunc(n):
				trunc_primes.append(n)
		n += 1
	print(sum(trunc_primes))
main()

# 748317
# Completed on Sun, 14 Mar 2021, 22:12
