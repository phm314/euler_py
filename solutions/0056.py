'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, 
what is the maximum digital sum?
'''

maxsum = 0
for a in range(1, 100):
  print(a)
  for b in range(1, 100):
    num = pow(a, b)
    st = str(num)
    disum = sum([int(i) for i in st])
    maxsum = max(maxsum, disum)

print(maxsum)

# 972
# Completed on Tue, 16 Mar 2021, 21:08
