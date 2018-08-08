#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.2a
Сделать копию скрипта задания 7.2.
Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys

try:
    with open(sys.argv[1], 'r') as config:
        for l in config:
            if not l.startswith('!'):
               f = True
               for e in ignore:
                 r=l.find(e)
                 if r != -1:
                   f = False
               if f:
                   print(l.rstrip())
except:
    print('No such file')
finally:
    config.close()
