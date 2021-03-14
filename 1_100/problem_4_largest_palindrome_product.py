pals = []
for i in range(100, 1000):
  for j in range(100, 1000):
    n = str(i*j)
    for c in range(len(n)):
      if n[c] != n[-c-1]:
        break
    else:
      pals.append(int(n))

print(max(pals))

# 906609
# Completed on Tue, 9 Feb 2021, 21:39
