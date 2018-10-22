# -*- coding: utf-8 -*-
'''
Задание 21.4

Создайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться
при необходимости добавить VLAN на коммутатор.

В шаблоне должны поддерживаться возможности:
* добавления VLAN и имени VLAN
* добавления VLAN как access, на указанном интерфейсе
* добавления VLAN в список разрешенных, на указанные транки

Если VLAN необходимо добавить как access,
то надо настроить и режим интерфейса и добавить его в VLAN:
interface Gi0/1
 switchport mode access
 switchport access vlan 5

Для транков, необходимо только добавить VLAN в список разрешенных:
interface Gi0/10
 switchport trunk allowed vlan add 5

Имена переменных надо выбрать на основании примера данных,
в файле data_files/add_vlan_to_switch.yaml.


Проверьте шаблон templates/add_vlan_to_switch.txt
на данных в файле data_files/add_vlan_to_switch.yaml,
с помощью функции generate_cfg_from_template из задания 21.1-21.1c.
Не копируйте код функции.
'''


import task_21_1c as gen
import sys

if __name__ == '__main__':
 template = sys.argv[1]
 fvars = sys.argv[2]
 r = gen.generate_cfg_from_template(template, fvars, trim_blocks=True, lstrip_blocks=True)
 #r = gen.generate_cfg_from_template(template, fvars, trim_blocks=False, lstrip_blocks=False)
 print(r)
