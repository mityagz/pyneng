#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-
'''
Задание 5.1
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

prefix=input("Enter ip prefix:")
net, mask = prefix.split("/")
ip0, ip1, ip2, ip3 = net.split(".")
tmask = {'24':'255.255.255.0', '16':'255.255.0.0','8':'255.0.0.0'}

print("Network:")
print("{:8>} {:8} {:8} {:8}".format(int(ip0), int(ip1), int(ip2), int(ip3)))
print("{:08b} {:08b} {:08b} {:08b}".format(int(ip0), int(ip1), int(ip2), int(ip3)))
print("Mask:")
print("/" + mask)
print("{:8>} {:8} {:8} {:8}".format(int(tmask['24'].split('.')[0]), int(tmask['24'].split('.')[1]), int(tmask['24'].split('.')[2]), int(tmask['24'].split('.')[3])))
print("{:08b} {:08b} {:08b} {:08b}".format(int(tmask[mask].split('.')[0]), int(tmask[mask].split('.')[1]), int(tmask[mask].split('.')[2]), int(tmask[mask].split('.')[3])))
