# -*- coding: utf-8 -*-
'''
Задание 19.4

Создать функцию send_commands_to_devices (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В этой функции должен использоваться список словарей, в котором не указаны имя пользователя, пароль, и пароль на enable (файл devices2.yaml).

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

Функция send_commands_to_devices должна использовать функцию send_commands из задания 19.3.

'''

commands_with_errors = ['set bgp', 'set system', 's']
correct_commands = ['set system location building NH', 'set system services netconf ssh']
error_out = ['syntax error.', 'missing argument.', 'is ambiguous.']

commands = commands_with_errors + correct_commands

import getpass
import sys
import yaml
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException
import task_19_3 as ss

def send_commands_to_devices(devices_list, show='', filename='', config=''):
 r = ss.send_commands(devices_list, show, filename, config)
 return r

if __name__ == "__main__":
 USER = input('Username: ')
 PASSWORD = getpass.getpass()

 with open('devices2.yaml', 'r') as f:
  y = yaml.load(f)
 print(y)
 for device in y['routers']:
  device['username'] = USER
  device['password'] = PASSWORD
  rr = send_commands_to_devices(device, show='run show bgp summary')
  #rr = send_commands_to_devices(device, config=correct_commands)
  #rr = send_commands_to_devices(device, filename='file_command')
  print(rr)
