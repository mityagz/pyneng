# -*- coding: utf-8 -*-
'''
Задание 22.4

На основе примера textfsm_clitable.py из раздела TextFSM
сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера, который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

Пример из раздела:
'''
import clitable


def parse_command_dynamic(attrs, idx, templates, commands):
 cli_table = clitable.CliTable('index', 'templates')

 cli_table.ParseCmd(output_sh_ip_route_ospf, attributes)


 data_rows = [list(row) for row in cli_table]
 header = list(cli_table.header)

 rr = []
 for r in data_rows:
   p = dict(zip(header, r))
   rr.append(p)
 return rr

if __name__ == '__main__':
 output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()
 attributes = {'Command': 'show ip route ospf', 'Vendor': 'cisco_ios'}
 r = parse_command_dynamic(attributes, 'index', 'templates', output_sh_ip_route_ospf)
 print(r)
