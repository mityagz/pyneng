#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-


result={}
with open("sh_ip_interface.txt", 'r') as f:
    for line in f:
        if 'line protocol' in line:
         interface, *other  = line.split()
        elif 'MTU' in line:
         _, _, mtu, *other = line.split()
         result[interface] = mtu

print(result)
