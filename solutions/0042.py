'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
# getting words.txt
from urllib.request import urlopen

def w():
	url = 'https://projecteuler.net/project/resources/p042_words.txt'
	with urlopen(url) as inf:
		pg = inf.read().decode()
		wds = pg.split(',')
		wds = [w.strip('"').lower() for w in wds]
	return wds
		
def tri(n):
	t = []
	for i in range(1, n):
		t.append(int(i * (i + 1) / 2))
	return tuple(t)
	
def chval(ch):
	return ord(ch) - 96

def wdval(wd):
	return sum([chval(ch) for ch in wd])
	
def main():
	sol = 0
	wds = w()
	tris = tri(100000)
	for wd in wds:
		if wdval(wd) in tris:
			sol += 1
	print(sol)
	
main()

# 162
# Completed on Tue, 16 Mar 2021, 17:05