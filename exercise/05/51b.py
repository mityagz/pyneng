#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-
import sys
from sys import	argv
'''
Задание 5.1b
Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

prefix = argv[1]
print(prefix)

net, s = prefix.split("/")
ip0, ip1, ip2, ip3 = net.split(".")
mask = [0, 0, 0, 0]
for i in range(int(s)):
 mask[int(i/8)] = mask[int(i/8)] + (1 << (7 - i % 8))

print("Network:")
print("{:8>} {:8} {:8} {:8}".format(int(ip0) & int(mask[0]), int(ip1) & int(mask[1]), int(ip2) & int(mask[2]), int(ip3) & int(mask[3])))
print("{:08b} {:08b} {:08b} {:08b}".format(int(ip0) & int(mask[0]), int(ip1) & int(mask[1]), int(ip2) & int(mask[2]), int(ip3) & int(mask[3])))
print("Mask:")
print("/" + s)
print("{:8>} {:8} {:8} {:8}".format(int(mask[0]), int(mask[1]), int(mask[2]), int(mask[3])))
print("{:08b} {:08b} {:08b} {:08b}".format(int(mask[0]), int(mask[1]), int(mask[2]), int(mask[3])))
