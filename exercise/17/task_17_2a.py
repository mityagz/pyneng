#!/home/python/n/pyneng/bin/python
import task_17_2 as pcdp
import glob
import yaml

# -*- coding: utf-8 -*-
'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''

sh_version_files = glob.glob('sh_cdp_n_*')

topology = {}

for ff in sh_version_files:
 with open(ff) as f:
  r = pcdp.parse_sh_cdp_neighbors(f.read())
  for k in r.keys():
   topology[k] = r[k]

print(topology)

with open('topology.yaml', 'w') as f:
 y = yaml.dump(topology, f)

'''
./task_17_2a.py 
{'SW1': {'Eth 0/1': {'R1': '2811'}, 'Eth 0/2': {'R2': '2811'}, 'Eth 0/3': {'R3': '2811'}, 'Eth 0/4': {'R4': '2811'}}, 'R1': {'Eth 0/0': {'SW1': 'WS-C3750-'}}, 'R4': {'Eth 0/0': {'SW1': 'WS-C3750-'}, 'Eth 0/1': {'R5': '2811'}}, 'R3': {'Eth 0/0': {'SW1': 'WS-C3750-'}}, 'R5': {'Eth 0/0': {'R2': '2811'}, 'Eth 0/1': {'R4': '2811'}}, 'R6': {'Eth 0/1': {'R2': '2811'}}, 'R2': {'Eth 0/0': {'SW1': 'WS-C3750-'}, 'Eth 0/1': {'R5': '2811'}, 'Eth 0/2': {'R6': '2811'}}}
'''
