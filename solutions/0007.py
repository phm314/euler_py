'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
from math import isqrt

def prime(x):
	n = 1
	primes = 0
	while primes < x:
		n += 1
		for j in range(2, isqrt(n) + 1):
			if n % j == 0:
				break
				
		else:
			primes += 1
			
	print(n)
prime(10001)

# 104743
# Completed on Thu, 11 Feb 2021, 07:12
