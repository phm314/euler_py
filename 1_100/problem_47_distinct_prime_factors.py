'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
from math import isqrt

def prime(n):
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			return False
	else:
		return True

def pfac(n, p = 4):
	pf = []
	for i in range(2, isqrt(n) +1):
		if n % i == 0:
			if prime(i):
				pf.append(i)
			if prime(n // i):
				pf.append(n // i)
	return len(set(pf)) >= p
	
def con():
	n = 0
	while True:
		if pfac(n) and pfac(n + 1) and pfac(n + 2) and pfac(n + 3):
			print(n)
			break
		n += 1
con()
# 134043
# Completed on Tue, 16 Mar 2021, 16:55