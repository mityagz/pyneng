#!/home/python/n/pyneng/bin/python

res = {}

def parse_cdp(filename):
 with open(filename) as f:
   for l in f:
     if l.startswith('Device ID:'):
       neib = l.split(': ')[1].split('\n')[0]
       res[neib] = {}
     elif l.startswith('  IP address:'):
       ip = l.split(': ')[1].split('\n')[0]
       res[neib]['ip'] = ip
     elif l.startswith('Platform: '):
       pl = ' '.join(l.split(': ')[1:3]).split('\n')[0]
       res[neib]['pl'] = pl
     elif l.startswith('Cisco IOS Software,'):
       res[neib]['v'] = l.split('\n')[0]
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
