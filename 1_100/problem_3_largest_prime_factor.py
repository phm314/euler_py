'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
from math import isqrt

def g(n):
  factors = []
  primes = []
  for i in range(1, isqrt(n) + 1):
    if n % i == 0:
      factors.append(i)
      factors.append(n // i)
  for i in factors:
    for j in range(2, isqrt(i) + 1):
      if i % j == 0:
        break
    else:
      primes.append(i)
  ans = max(primes)
  print(ans)
        
big = 600851475143
g(big)
# 6857
# Completed on Tue, 9 Feb 2021, 20:54
