#!/usr/bin/env python3 

import sys
from shlex import split

ips={}

with open("/var/log/auth.log") as f:

  for line in f.readlines():

    if ("invalid" in line):
      m=line.split()

      try:
        ip=m[m.index("port")-1]
        username=m[m.index("user")+1]

        if (ip not in ips):
          ips[ip]=""

        if (username not in ips[ip]):
          ips[ip]=ips[ip]+username+" "

      except:
        pass

for ip in ips:
  print  (ip,":",ips[ip])

