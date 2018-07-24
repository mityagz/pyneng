# -*- coding: utf-8 -*-
'''
Задание 4.6
Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'


In [370]: ospf_route='O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [371]: route=ospf_route.replace('O', 'OSPF').replace(',', '').split()

In [372]: r0={'Protocol': route[0], 'Prefix': route[1], 'AD/Metric': route[2], 'Next-Hop': route[4], 'Last update': route[5], 'Outbount interface': route[6]}

In [373]: print("Protocol:{:>30}\nPrefix:{:>30}\nAD/Metric:{:>30}\nNext-Hop:{:>30}\nLast update:{:>30}\nOutbount interface:{:>30}\n".format(r0['Protocol'], r0['Prefix
     ...: '], r0['AD/Metric'], r0['Next-Hop'], r0['Last update'], r0['Outbount interface']))
Protocol:                          OSPF
Prefix:                  10.0.24.0/24
AD/Metric:                      [110/41]
Next-Hop:                     10.0.13.3
Last update:                         3d18h
Outbount interface:               FastEthernet0/0
