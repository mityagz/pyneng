#!/home/python/n/pyneng/bin/python

import re

port = set()

with open("log.txt") as l:
     for line in l:
       match = re.match('\S+ Host (\S+).*vlan (\d+).*port (\S+) and port (\S+)', line)
       if match:
        vlan = match.group(2)
        port.add(match.group(3))
        port.add(match.group(4))

print('Loop between ports {} in vlan {}'.format(', '.join(port), vlan))
