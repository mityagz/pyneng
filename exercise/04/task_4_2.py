# -*- coding: utf-8 -*-
'''
Задание 4.2
Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

MAC = 'AAAA:BBBB:CCCC'

In [288]: MAC='AAAA:BBBB:CCCC'

In [289]: MAC.replace(':','.')
Out[289]: 'AAAA.BBBB.CCCC'
