''''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from math import isqrt, sqrt

def prime(n):
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			return False
	else:
		return True

def sqr(n):
	s = sqrt(n)
	return s == int(s)
	
n = 3
run = True
while run:
	if not prime(n) and n % 2 == 1:
		for p in range(2, n):
			if prime(p):
				rem = n - p
				if sqr(rem/2):
					break
		else:
			print(n)
			run = False
	n += 1
	
# 5777
# Completed on Tue, 16 Mar 2021, 17:07