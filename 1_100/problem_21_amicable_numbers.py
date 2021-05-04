'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import isqrt

def d(n):
  ret = []
  for i in range(1, isqrt(n) + 1):
    if not n % i:
      ret.append(i)
      if n // i != n:
        ret.append(n // i)
  return sum(ret)

def m():
  sol = []
  for i in range(1,10000):

    a = d(i)

    if a != 1:
      b = d(a)

      if a != b and b == i:
        print(i, a, b)
        sol.append(i)
  return sum(sol)
ans = m()
print(ans)

# 31626
# Completed on Tue, 4 May 2021, 21:10
