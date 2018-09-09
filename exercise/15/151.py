#!/home/python/n/pyneng/bin/python

import re
import sys

res = {}

regex = sys.argv[1]
filename = sys.argv[2]

def parse(filename, regex):
 with open(filename) as f:
   for l in f:
     match = re.search(regex, l)
     if match:
      print(l.rstrip())
 return res

if __name__ == '__main__':
  parse(filename, regex)
