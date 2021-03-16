'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''


from urllib.request import urlopen

url = 'https://projecteuler.net/project/resources/p022_names.txt'
page = urlopen(url).read().decode()
l = page.split(',')
name = [i.strip('"') for i in l]
name.sort()
sum = 0

for i, n in enumerate(name):
	k = 0
	for j in n:
		k += ord(j)-64
	sum += k * (i + 1)
print(sum)

# 871198282
# Completed on Thu, 11 Feb 2021, 23:00
