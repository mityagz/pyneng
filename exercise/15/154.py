#!/home/python/n/pyneng/bin/python

import re
import sys

filename = sys.argv[1]

res = []

# Interface IP-Address Status Protocol

# Interface                  IP-Address      OK? Method Status                Protocol
# FastEthernet0/0            15.0.15.1       YES manual up                    up

def parse_sh_ip_int_br(filename):
 with open(filename) as f:
   for l in f:
     match = re.match('(?P<intf>\S+)\s+(?P<ip>(?:(?:(?:\d+){1,3}.){3}(?:\d+){1,3})|unassigned)\s+\S+\s+\S+\s+(?P<status>up|.*down)\s+(?P<proto>up|down)', l)
     if match:
         res.append(match.group('intf', 'ip', 'status', 'proto'))
 return res

if __name__ == '__main__':
 print(parse_sh_ip_int_br(filename))


#./154.py sh_ip_int_br_2.txt 
#[('FastEthernet0/0', '15.0.15.1', 'up', 'up'), ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),  \
# ('FastEthernet0/2', '10.0.13.1', 'up', 'up'), ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'), ('Loopback0', '10.1.1.1', 'up', 'up'), ('Loopback100', '100.0.0.1', 'up', 'up')]
