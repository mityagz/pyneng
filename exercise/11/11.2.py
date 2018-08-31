#!/home/python/n/pyneng/bin/python

import draw_network_graph as draw
import parse_cdp_neighbors as parse

s1 = {}
with open('sw1_sh_cdp_neighbors.txt') as f:
   s1 = parse.parse_cdp_neighbors(f.read())
   draw.draw_topology(s1, "sw1_topo")
