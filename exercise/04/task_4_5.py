# -*- coding: utf-8 -*-
'''
Задание 4.5
Список VLANS это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

In [364]: VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

In [365]: s=set(VLANS)

In [366]: v=list(s)

In [367]: v
Out[367]: [1, 2, 3, 100, 4, 10, 20, 30]

In [368]: v.sort()

In [369]: v
Out[369]: [1, 2, 3, 4, 10, 20, 30, 100]
