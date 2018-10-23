# -*- coding: utf-8 -*-
'''
Задание 22.3

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding.
Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* MacAddress
* IpAddress
* VLAN
* Interface

Проверить работу шаблона с помощью функции из задания 22.1.
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
 header = r[0]
 print(tabulate(r[1], headers=header))
 #print(tabulate(r[1]))
