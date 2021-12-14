'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example,
3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from math import sqrt
a,b,c = 1,1,0

while a < 1000:
	while b < 1000:
		c = sqrt(a **2 + b ** 2)
		if c == int(c):
			if a+b+c == 1000:
				print(a,b,c,a*b*c)
				a = 1000
		b+=1
	a,b = a+1,a
	
# 31875000
# Completed on Thu, 11 Feb 2021, 07:14
