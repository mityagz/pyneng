#!/home/python/n/pyneng/bin/python

import re
import sys

filename = sys.argv[1]

res = []

def parse_cfg(filename):
 with open(filename) as f:
   for l in f:
     match = re.match(' ip address ((?:(?:\d+){1,3}.){3}(?:\d+){1,3}) ((?:(?:\d+){1,3}.){3}(?:\d+){1,3}).*', l)
     if match:
        res.append(match.group(1, 2)) 
 return res

if __name__ == '__main__':
 print(parse_cfg(filename))

#./153.py config_r1.txt 
#[('10.1.1.1', '255.255.255.255'), ('10.0.13.1', '255.255.255.0'), ('10.0.19.1', '255.255.255.0')]
