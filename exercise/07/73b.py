#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import sys

mac = {}
camline = []

try:
 with open('CAM_table.txt', 'r') as cam:
        for l in cam:
          if l.find('.') != -1:
            m = l.split()
            if not m[0] in mac:
             mac[m[0]] = []
            mac[m[0]].append((m[1], m[2], m[3]))


 vlan=input('Enter vid number:')

 for i0, i1 in mac.items():
   if vlan == i0:
    for i in mac[i0]:
     print(i0, i[0], i[1], i[2])

except:
    print('No such file')
finally:
    cam.close()
