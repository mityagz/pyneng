# -*- coding: utf-8 -*-
'''
Задание 22.2

В этом задании нужно использовать функцию parse_output из задания 22.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки
команды sh ip int br (шаблон и вывод есть в разделе).
'''

import sys
import textfsm
from tabulate import tabulate
import csv

def parse_output(tmpl, showcmd):
 r = []
 with open(tmpl) as f:
     re_table = textfsm.TextFSM(f)
     header = re_table.header
     result = re_table.ParseText(showcmd)
     for e in result:
      rr = dict(zip(header, e))
      r.append(rr)
 return r

def list_to_csv(dct, fout):
 with open(fout, 'w') as f:
  w = csv.DictWriter(f, dct[0])
  w.writeheader()
  for d in dct:
   w.writerow(d)


if __name__ == '__main__':
 template = sys.argv[1]
 output_file = sys.argv[2]
 fout = sys.argv[3]
 with open(output_file, 'r') as f:
  o = f.read()
  r = parse_output(template, o)
 print(r)
 list_to_csv(r, fout)
