#!/usr/bin/env python3

def fibo(i):
  if (i<=1): return(1)
  else: return(fibo(i-1)+fibo(i-2))

a=1
for i in range(1,30):
  b=a
  a=fibo(i)
  print (f"{b:20} {a:20}     {float(a)/float(b):<20}")
