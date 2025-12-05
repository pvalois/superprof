#!/usr/bin/env python3 

def kfibo(n, k=2):
    a = list(range(k))   # conditions initiales: 0,1,2,3,4

    if n < k:
        return a[n]

    for _ in range(n - (k-1)):
        s = sum(a)
        a = a[1:] + [s]

    return a[-1]

for i in range(1, 100):
  print (i,end=" ")
  for k in range(2,15):
      print(f"{kfibo(i,k)/kfibo(i+1,k):1.7}",end=" ")
  print ()


