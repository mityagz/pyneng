#!/home/python/n/pyneng/bin/python

import re
import sys
import parse_sh_ip_int_br as p

filename = sys.argv[1]

res = []
res2 = []

headers = ['interface', 'address', 'status', 'protocol']
res = p.parse_sh_ip_int_br(filename)

def convert_to_dict(headers, res):
 for i in res:
  res2.append(dict(zip(headers, i)))
 return res2
  

if __name__ == '__main__':
 print(convert_to_dict(headers, res))
