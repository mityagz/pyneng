#!/home/python/n/pyneng/bin/python

import re

res = {}

regex = 'Device ID: (?P<dev>\S+)|IP address: (?P<ip>\S+)|Platform: (?P<p>\S+)|Cisco IOS Software, (?P<ios>.+), RELEASE'

def parse_cdp(filename):
 with open(filename) as f:
   for l in f:
     match = re.search(regex, l)
     if match:
      print(match.lastgroup)
      if match.lastgroup == 'dev':
         dev = match.group(match.lastgroup)
         res[dev] = {}
      elif dev:
         res[dev][match.lastgroup] = match.group(match.lastgroup)
 print(regex)
 return res

'''
SW1#show cdp neighbors detail
-------------------------
Device ID: SW2
Entry address(es):
  IP address: 10.1.1.2
Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 164 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Mon 03-Mar-14 22:53 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 10.1.1.2
'''

if __name__ == '__main__':
 print(parse_cdp('sh_cdp_neighbors_sw1.txt'))
