#!/home/python/n/pyneng/bin/python

import re

port = set()

regex = 'Host (\S+).*vlan (\d+).*port (\S+) and port (\S+)'

with open("log.txt") as f:
 s = f.read()
 result = re.finditer(regex, s)
 for m in result:
  if m:
   port.add(m.group(3))
   port.add(m.group(4))
print('Loop between ports {} in vlan {}'.format(', '.join(port), m.group(2)))
