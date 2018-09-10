#!/home/python/n/pyneng/bin/python

import re
import sys

filename = sys.argv[1]

res = {}



def parse_cfg(filename):
 with open(filename) as f:
   for l in f:
     match = re.match('interface (?P<intf>\S+)| ip address (?P<ip>(?:(?:\d+){1,3}.){3}(?:\d+){1,3}) (?P<mask>(?:(?:\d+){1,3}.){3}(?:\d+){1,3}).*', l)
     if match:
       if match.lastgroup == 'intf':
         intf = match.group(match.lastgroup)
         res[intf] = []
       elif intf:
         res[intf].append( match.group('ip', 'mask'))
 return res

if __name__ == '__main__':
 print(parse_cfg(filename))


#./153b.py config_r2.txt 
#{'Loopback0': [('10.2.2.2', '255.255.255.255')], 'Tunnel0': [], 'Ethernet0/0': [('10.0.23.2', '255.255.255.0')], 'Ethernet0/1': [('10.255.2.2', '255.255.255.0'), ('10.254.2.2', '255.255.255.0')], 'Ethernet0/2': [('10.0.29.2', '255.255.255.0')], 'Ethernet0/3': [], 'Ethernet0/3.100': [], 'Ethernet1/0': []}
