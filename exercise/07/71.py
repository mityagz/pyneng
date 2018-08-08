#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

with open("ospf.txt", 'r') as rt:
    for l in rt:
        route = l.replace('O', 'OSPF').replace(',', '').split()
        route0 = {'Protocol': route[0], 'Prefix': route[1], 'AD/Metric': route[2], 'Next-Hop': route[4], 'Last update': route[5], 'Outbount interface': route[6]}
        print("Protocol:{:>30}\nPrefix:{:>30}\nAD/Metric:{:>30}\nNext-Hop:{:>30}\nLast update:{:>30}\nOutbount interface:{:>30}\n".format(route0['Protocol'], route0['Prefix'], route0['AD/Metric'], route0['Next-Hop'], route0['Last update'], route0['Outbount interface']))

