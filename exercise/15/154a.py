#!/home/python/n/pyneng/bin/python

import re
import sys
import parse_sh_ip_int_br as p

filename = sys.argv[1]

res = []
res2 = []

# Interface IP-Address Status Protocol
# Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            15.0.15.1       YES manual up                    up

headers = ['interface', 'address', 'status', 'protocol']
res = p.parse_sh_ip_int_br(filename)

def convert_to_dict(headers, res):
 for i in res:
  d = {}
  j = 0
  for e in i:
   d[headers[j]] = e
   j += 1
  res2.append(d)
 return res2
  

if __name__ == '__main__':
 print(convert_to_dict(headers, res))
