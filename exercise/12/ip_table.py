#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 12.3
Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.
Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.
'''

import check_ip_availability as cia
from tabulate import tabulate

l = ['127.0.0.1-127.0.0.4', '128.0.0.2-4', '127.0.0.17' , '128.0.0.1']

array_inp = []

def ip_table(r):
 columns=['Reachable', 'Unreachable']
 reach_len = len(r[0])
 unreach_len = len(r[1])
 if reach_len > unreach_len:
  max_len = reach_len
 else:
  max_len = unreach_len
 tab = []
 i = 0
 while i < reach_len:
  try:
    re = r[0][i]
  except:
    re = ''
  try:
    ure = r[1][i]
  except:
    ure = ''
  tab.append([ re, ure ] )
  i += 1
 print(tabulate(tab, headers=columns))


if __name__ == '__main__':
 print(l)
 ip_table(cia.check_ip_availability(l))
