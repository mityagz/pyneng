# -*- coding: utf-8 -*-
'''
Задание 4.7
Преобразовать MAC-адрес в двоичную строку (без двоеточий).
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

MAC = 'AAAA:BBBB:CCCC'

In [381]: MAC='AAAA:BBBB:CCCC'

In [382]: bin(int(MAC.replace(':',''),16)).replace('0b','')
Out[382]: '101010101010101010111011101110111100110011001100'
