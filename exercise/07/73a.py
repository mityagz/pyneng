#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.3a
Сделать копию скрипта задания 7.3.
Дополнить скрипт:
- Отсортировать вывод по номеру VLAN
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import sys

camline = []
try:
 with open('CAM_table.txt', 'r') as cam:
        for l in cam:
          if l.find('.') != -1:
            m = l.split()
            camline.append(l.rstrip())

 for l in sorted(camline):
  print(l)

except:
    print('No such file')
finally:
    cam.close()
