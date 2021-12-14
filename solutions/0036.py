'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
def pal(st):
	for n in range(len(st)):
		if st[n] != st[-n-1]:
			return False
	return True

def main():
	sum = 0
	for i in range(1000001):
		n = str(i)
		b = str(bin(i)).split('b')[1]
		if pal(n) and pal(b):
			sum += i
	print(sum)

main()

# 872187
# Completed on Sun, 14 Mar 2021, 22:19
