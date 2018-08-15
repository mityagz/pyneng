#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-


result={}
with open("sh_ip_int_br.txt", 'r') as f:
    for l in f:
        line = l.split()
        if line and line[1][0].isdigit(): 
         interface, ip, *other  = line
         result[interface]=ip

print(result)
