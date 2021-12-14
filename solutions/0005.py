'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# brute force approach
n = 22
while True:
  for i in range(2, 21):
    if n % i != 0:
      break
  else:
    print(n)
    break

  n += 1
    
# 232792560
# Completed on Tue, 16 Mar 2021, 20:18
