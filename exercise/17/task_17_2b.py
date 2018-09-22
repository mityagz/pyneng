#!/home/python/n/pyneng/bin/python

# -*- coding: utf-8 -*-

import task_17_2 as pcdp
import glob
import yaml


'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''

def generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology.yaml'):
 topology = {}
 for ff in sh_version_files:
  with open(ff) as f:
   r = pcdp.parse_sh_cdp_neighbors(f.read())
   print(r)
   for k in r.keys():
    topology[k] = r[k]


  if save_to_file:
   with open(topology_filename, 'w') as f:
    y = yaml.dump(topology, f)


 print(topology)
 return topology


if __name__ == '__main__':
 sh_version_files = glob.glob('sh_cdp_n_*')
 print(generate_topology_from_cdp(sh_version_files))
