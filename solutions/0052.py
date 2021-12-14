'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
n = 1
while True:
	nums = set(str(n))
	for i in range(2, 7):
		num = n * i
		if set(str(num)) != nums:
			break
	else:
		print('sol:', n)
		break
	n += 1

# 142857
# Completed on Tue, 16 Mar 2021, 17:59