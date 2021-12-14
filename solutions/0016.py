'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''
sol = sum(int(i) for i in str(2**1000))
print(sol)
# 1366
# Completed on Thu, 11 Feb 2021, 09:19
