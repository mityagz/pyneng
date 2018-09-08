#!/home/python/n/pyneng/bin/python

import re

port = set()

regex = 'Host (\S+).*vlan (\d+).*port (\S+) and port (\S+)'

result = []

with open("log.txt") as f:
 s = f.read()
 result = re.findall(regex, s)
 for l in result:
   port.add(l[2])
   port.add(l[3])
print('Loop between ports {} in vlan {}'.format(', '.join(port), l[1]))
