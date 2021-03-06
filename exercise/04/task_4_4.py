# -*- coding: utf-8 -*-
'''
Задание 4.4
Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.
Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'


In [345]: s = list(set([ int(vlan) for vlan in command1.split()[4].split(',') if vlan.isdigit() ]) & set([ int(vlan) for vlan in command2.split()[4].split(',') if vla
     ...: n.isdigit() ]))

In [346]: s
Out[346]: [1, 3, 100]
