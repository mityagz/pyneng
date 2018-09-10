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
  res2.append(dict([(headers[0], i[0]), (headers[1], i[1]), (headers[2], i[2]), (headers[3], i[3])]))
 return res2
  

if __name__ == '__main__':
 print(convert_to_dict(headers, res))
