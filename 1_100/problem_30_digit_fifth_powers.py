'''
Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
'''
ans = []
for i in range(2, 1000000):
	n = str(i)
	s = 0
	for a in n:
		s += pow(int(a), 5)
	if s == i:
		ans.append(s)

s = 0
for i in ans:
	s += i
	
print(s)

# 443839
# Completed on Sun, 14 Mar 2021, 06:17
