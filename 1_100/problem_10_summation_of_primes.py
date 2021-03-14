'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
from math import isqrt
s = 0
for i in range(2, 2000000):
	for j in range(2, isqrt(i) + 1):
		if i % j == 0:
			break
	else:
		s += i
print(s)

# 142913828922
# 142913828920 + 2
# Completed on Thu, 11 Feb 2021, 07:15
