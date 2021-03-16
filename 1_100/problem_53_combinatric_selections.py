'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation,

C(5, 3) = 10

In general,
C(n, r) = n!/(r!(n-r)!), where r <= n, n! = n * (n - 1)... * 1 and 0! = 1.

It is not until
n = 23, that a value exceeds one-million: C(23, 10).

How many, not necessarily distinct, values of C(n, r)
for 1 <= 1 <= 100, are greater than one-million?
'''
from math import factorial as f

def c(n, r):
  res = f(n) / (f(r) * f(n - r))
  return res

sol = 0
for n in range(1, 101):
  for r in range(n):
    num = c(n, r)
    if num > 1000000:
      print(n, r)
      sol += 1
  n += 1
print(sol)

# 4075
# Completed on Tue, 16 Mar 2021, 20:42
