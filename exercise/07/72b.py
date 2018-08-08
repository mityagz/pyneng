#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys

try:
    with open(sys.argv[1], 'r') as config, open('config_sw1_cleared.txt', 'w') as outconf:
        for l in config:
               f = True
               for e in ignore:
                 r=l.find(e)
                 if r != -1:
                   f = False
               if f:
                   outconf.write(l)
except:
    print('No such file')
finally:
    config.close()
