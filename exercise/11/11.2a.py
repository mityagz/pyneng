#!/home/python/n/pyneng/bin/python

import draw_network_graph as draw
import parse_cdp_neighbors as parse

s = {}
r = {}
flist = [ 'sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt' ]
#flist = [ 'sh_cdp_n_r1.txt' ]
#flist = [ 'sh_cdp_n_sw1.txt' ]
t = 0

for fl in flist:
 with open(fl) as f:
   s1 = {}
   s1 = parse.parse_cdp_neighbors(f.read())
   for k, v in s1.items():
        if len(s) == 0:
         s[k] = v
         r[v] = k
        else:
           try:
            r[k]
           except: 
            s[k] = v
            r[v] = k

draw.draw_topology(s, "sw_topo")
