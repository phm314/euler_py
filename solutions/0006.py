'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + 3**2 ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''
def dif(n):
	sumsq = sum(i**2 for i in range(n+1))
	sqsum = sum(range(n+1))**2
	return sqsum-sumsq
	
print(dif(100))
# 25164150
# Completed on Thu, 11 Feb 2021, 07:03
