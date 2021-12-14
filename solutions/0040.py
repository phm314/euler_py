'''
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
a = ''
n = 1
while len(a) < 1000000:
	a += str(n)
	n += 1

id = [1, 10, 100, 1000, 10000, 100000, 1000000]

prod = 1
for i in id:
	prod *= int(a[i - 1])
	
print(prod)

# 210
# Completed on Tue, 16 Mar 2021, 16:59