# -*- coding: utf-8 -*-
'''
Задание 22.4a

Переделать функцию из задания 22.4:
* добавить аргумент show_output, который контролирует будет ли выводится результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться с помощью FormattedTable (пример есть в разделе)

'''

import clitable


def parse_command_dynamic(attrs, idx, templates, commands, show_output=False):
 cli_table = clitable.CliTable('index', 'templates')

 cli_table.ParseCmd(commands, attrs)


 data_rows = [list(row) for row in cli_table]
 header = list(cli_table.header)

 rr = []
 for r in data_rows:
   p = dict(zip(header, r))
   rr.append(p)
 if show_output:
  print('CLI Table output:\n', cli_table)
  print('Formatted Table:\n', cli_table.FormattedTable())
 return rr

if __name__ == '__main__':
 output_sh_ip_route_ospf = open('output/sh_ip_route_ospf.txt').read()
 attributes = {'Command': 'show ip route ospf', 'Vendor': 'cisco_ios'}
 r = parse_command_dynamic(attributes, 'index', 'templates', output_sh_ip_route_ospf, True)
