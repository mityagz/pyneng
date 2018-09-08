#!/home/python/n/pyneng/bin/python

import re

port = set()

regex_src = 'Host (\S+).*vlan (\d+).*port (\S+) and port (\S+)'

result = []

with open("log.txt") as f:
 regex = re.compile(regex_src)
 for l in f:
   match = regex.search(l)
   if match:
     port.add(match.group(3))
     port.add(match.group(4))
print('Loop between ports {} in vlan {}'.format(', '.join(port), match.group(2)))
