#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-


result={}
with open("sh_ip_interface2.txt", 'r') as f:
    for line in f:
        if 'line protocol' in line:
         interface, *other  = line.split()
        elif 'Internet address' in line:
         _, _, _, ip = line.split()
         result[interface] = {}
         result[interface]['ip'] = ip
        elif 'MTU' in line:
         _, _, mtu, *other = line.split()
         result[interface]['mtu'] = mtu

print(result)
