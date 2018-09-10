#!/home/python/n/pyneng/bin/python

import re
import sys

regex = sys.argv[1]
filename = sys.argv[2]

res = []

def return_match(regex, filename):
 with open(filename) as f:
   for l in f:
     match = re.search(regex, l)
     if match:
        res.append(match.group()) 
 print(regex)
 return res

if __name__ == '__main__':
 print(return_match(regex, filename))


#./152.py '((?:(?:\d+){1,3}.){3}(?:\d+){1,3})' sh_ip_int_br.txt
#((?:(?:\d+){1,3}.){3}(?:\d+){1,3})
#['15.0.15.1', '10.0.12.1', '10.0.13.1', '10.1.1.1', '100.0.0.1']
