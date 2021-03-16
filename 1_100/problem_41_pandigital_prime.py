'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from math import isqrt
from itertools import permutations

def prime(n):
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			break
	else:
		return True

def pan(n):
	s = str(n)
	return len(s) == len(set(s))
	
digits = '123456789'
for i in range(1, len(digits) + 1):
	nums = permutations(digits[:i])
	maxn = 0
	for j in nums:
		n = int(''.join(j))
		if prime(n) and pan(n):
			maxn = max(maxn, n)
	print(i, maxn)

# 7652413
# Completed on Tue, 16 Mar 2021, 17:01