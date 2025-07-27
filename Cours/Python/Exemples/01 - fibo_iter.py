#!/usr/bin/env python3

a=1.0
b=1.0

for i in range(30):
  c=a+b
  a=b
  b=c
  print (f"{a:20} {b:20}     {float(b)/float(a):<20}")
