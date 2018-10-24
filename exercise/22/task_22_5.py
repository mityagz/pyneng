# -*- coding: utf-8 -*-
'''
Задание 22.5

В этом задании соединяется функциональность TextFSM и подключение к оборудованию.

Задача такая:
* подключиться к оборудованию
* выполнить команду show
* полученный вывод передавать на обработку TextFSM
* вернуть результат обработки

Для этого, воспользуемся функциями, которые были созданы ранее:
* функцией send_show_command из упражнения 19.1
* функцией parse_command_dynamic из упражнения 22.4

В этом упражнении нужно создать функцию send_and_parse_command:
* функция должна использовать внутри себя функции parse_command_dynamic и send_show_command.
* какие аргументы должны быть у функции send_and_parse_command, нужно решить самостоятельно
 * но, надо иметь в виду, какие аргументы ожидают две готовые функции, которые мы используем
* функция send_and_parse_command должна возвращать:
 * функция send_show_command возвращает словарь с результатами выполнения команды:
    * ключ - IP устройства
    * значение - результат выполнения команды
 * затем, нужно отправить полученный вывод на обработку функции parse_command_dynamic
 * в результате, должен получиться словарь, в котором:
    * ключ - IP устройства
    * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции send_show_command создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command на команде sh ip int br.
'''

import sys
sys.path.insert(0, '../19/')
import task_22_4a as parse
import task_19_1 as send
import yaml


def send_and_parse_command(fdev, attributes, idx, tmpl, command, verbose): 

 USER = 'cisco'
 PASSWORD = 'cisco5'

 print(fdev)

 with open('devices2.yaml', 'r') as f:
  y = yaml.load(f)
  
  for r in y['routers']:
   r['username'] = USER
   r['password'] = PASSWORD

  rrr = {}
  #for device in y['routers']:
  #r = send.send_show_command(device, command)
  r = send.send_show_command(fdev, command)
  for k in r.keys():
   rr =  parse.parse_command_dynamic(attributes, idx, tmpl, r[k], verbose)
   rrr[k] = rr
 return rrr

if __name__ == '__main__':
 #command = 'run show system uptime | match Up'
 #command = 'run show interfaces brief'
 command = 'run show route table inet.0'
 attributes = {'Command': 'run show int brief', 'Vendor': 'junos'}
 r = send_and_parse_command('devices2.yaml', attributes, 'index', 'templates', command, False)
 for k in r.keys():
  print(k, r[k])
