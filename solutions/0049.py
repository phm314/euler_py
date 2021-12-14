'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
from math import isqrt
from itertools import combinations_with_replacement, permutations

def prime(n):
	for i in range(2, isqrt(n) + 1):
		if not n % i:
			return False
	return True

def combs():
	nums = [''.join(i) for i in combinations_with_replacement('1234567890', 4)]
	nums = [i for i in nums if len([n for n in i if n == '0']) < 3 and len(set(i)) > 1]
	return nums
	
def pattern(n):
	n.sort()
	for a in range(len(n)):
		na = n[a]
		for b in range(a+1, len(n)):
			nb = n[b]
			for c in range(b+1, len(n)):
				nc = n[c]
				if nc - nb == nb - na:
					print(''.join([str(na),str(nb),str(nc)]))
					print(nc-nb, nb-na)
				
def main():
	c = combs()
	for num in c:
		p = permutations(num)
		poss = []
		for i in p:
			i = int(''.join(i))
			if prime(i) and len(str(i)) == 4:
				poss.append(i)
		no_repeat = set(poss)
		if len(no_repeat) >= 3:
			pattern([*no_repeat])
			
main()

# 296962999629
# Completed on Tue, 16 Mar 2021, 16:50