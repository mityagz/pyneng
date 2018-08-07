#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 6.1
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip=input("Enter ip addreess: ")
ip0, ip1, ip2, ip3 = ip.split('.')
c = "unused"

if int(ip0) in range(1, 127):
 c = 'A'
elif int(ip0) in range(128, 191):
 c = 'B'
elif int(ip0) in range(192, 223):
 c = 'C'
elif int(ip0) in range(224, 239):
 c = 'D'
elif int(ip0) == 0:
 c = 'UNA'
elif int(ip0) == 255:
 c = 'LB'
else :
 c = 'UNU'

h = { 'A': 'unicast', 'B': 'unicast', 'C': 'unicast', 'D': 'multicast', 'UNA': 'unassigned', 'LB': 'local broadcast', 'UNU': 'unused' }

print(h[c])
