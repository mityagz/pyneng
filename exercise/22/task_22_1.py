# -*- coding: utf-8 -*-
'''
Задание 22.1

Переделать пример, который использовался в разделе TextFSM, в функцию.

Функция должна называться parse_output. Параметры функции:
* template - шаблон TextFSM (это должно быть имя файла, в котором находится шаблон)
* output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов (в примере ниже, находится в переменной header)
* остальные элементы это списки, в котором находятся результаты обработки вывода (в примере ниже, находится в переменной result)

Проверить работу функции на каком-то из примеров раздела.

Пример из раздела:
'''

import sys
import textfsm
from tabulate import tabulate

def parse_output(tmpl, showcmd):
 with open(tmpl) as f:
     re_table = textfsm.TextFSM(f)
     header = re_table.header
     result = re_table.ParseText(showcmd)
 return [ header, result ]



if __name__ == '__main__':
 template = sys.argv[1]
 output_file = sys.argv[2]
 with open(output_file, 'r') as f:
  o = f.read()
  r = parse_output(template, o)
 print(r)
