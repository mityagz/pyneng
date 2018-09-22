#!/home/python/n/pyneng/bin/python

# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

import re
import sys

def parse_sh_cdp_neighbors(sh_cdp):
 result = {}
 nei = {}
 sh_cdp_list = sh_cdp.split('\n')
 for l in sh_cdp_list:
  h = re.search('(?P<host>\S+)>show cdp neighbors', l)
  if h:
   host = h.group('host')
  n = re.search('(?P<nhost>\S+)\s+(?P<lintf>\w+\s?\S+)\s+\d+\s+(\w )+\s+\S+\s+(?P<nintf>\w+\s?\S+)', l)
  if n:
   nhost, lintf, nintf = n.group('nhost', 'lintf', 'nintf')
   nei[lintf] = {nhost: nintf}

 result[host] = nei

 return result


if __name__ == '__main__':
 with open(sys.argv[1]) as f:
  sh_cdp = f.read()
 print(parse_sh_cdp_neighbors(sh_cdp))

'''
./task_17_2.py sh_cdp_n_sw1.txt 
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'}, 'Eth 0/2': {'R2': 'Eth 0/0'}, 'Eth 0/3': {'R3': 'Eth 0/0'}, 'Eth 0/4': {'R4': 'Eth 0/0'}}}
'''
