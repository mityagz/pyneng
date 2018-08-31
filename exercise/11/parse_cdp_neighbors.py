#!/home/python/n/pyneng/bin/python


def parse_cdp_neighbors(cdp_neib):
  root = ""
  cdp_parsed = {}
  cdp_neib_lines = ignore_lines(cdp_neib.split('\n'))
  for l in cdp_neib_lines:
    if 'show cdp neighbors' in l:
     root = l.split(">")[0]
    else:
     neib = l.split('       ')
     s = tuple([root, neib[1].lstrip()])
     d = tuple([neib[0], neib[5]])
     cdp_parsed[s] = d
  return cdp_parsed




def ignore_lines(l):
 r = []
 for i in l:
  if not 'Capability Codes:' in i and not 'Device ID' in i and not 'S - Switch, H - Host, I - IGMP, r - Repeater, ' in i:
   if i == '':
    pass
   else:
    r.append(i)
 return r

if __name__ == '__main__':
 with open('sw1_sh_cdp_neighbors.txt') as f:
   print(parse_cdp_neighbors(f.read()))

