# -*- coding: utf-8 -*-
'''
Задание 22.1a

Переделать функцию parse_output из задания 22.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.
'''

import sys
import textfsm
from tabulate import tabulate

def parse_output(tmpl, showcmd):
 r = []
 with open(tmpl) as f:
     re_table = textfsm.TextFSM(f)
     header = re_table.header
     result = re_table.ParseText(showcmd)
     for e in result:
      rr = {}
      i = 0
      for h in header:
       rr[h] = e[i]
       i = i + 1
      r.append(rr)
 return r


if __name__ == '__main__':
 template = sys.argv[1]
 output_file = sys.argv[2]
 with open(output_file, 'r') as f:
  o = f.read()
  r = parse_output(template, o)
 print(r)
