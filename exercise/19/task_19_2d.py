# -*- coding: utf-8 -*-
'''
Задание 19.2d

В этом задании надо создать функцию send_cfg_to_devices, которая выполняет команды на нескольких устройствах последовательно и при этом выполняет проверку на ошибки в командах.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* config_commands - список команд, которые надо выполнить

Функция должна проверять результат на такие ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, функция должна выводить сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

После обнаружения ошибки, функция должна спросить пользователя надо ли выполнять эту команду на других устройствах.

Варианты ответа [y]/n:
* y - выполнять команду на оставшихся устройствах (значение по умолчанию)
* n - не выполнять команду на оставшихся устройствах

Функция send_cfg_to_devices должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение - вложенный словарь:
  * ключ - команда
  * значение - вывод с выполнением команд

В файле задания заготовлены команды с ошибками и без:
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


def send_config_command(device, command, verbose=True):
 r = {}
 re = {}
 flagErr = False
 DEVICE_PARAMS = device
 COMMAND = command
 print('Connection to device {}'.format(device['ip']))
 try:
  with ConnectHandler(**DEVICE_PARAMS) as ssh:
   ssh.config_mode()
   for c in COMMAND:
    result = ssh.send_command(c, strip_command=verbose)
    for errstr in error_out:
     if errstr in result:
      flagErr = True
      re[c] = []
      re[c].append(result)
      print(result)
      cont = input('Error occured. Do you want continue ? [y]/n: ') or 'y'
      if(cont == 'n'):
       exit(1)
    if(not flagErr):
     ssh.commit()	
     r[c] = []
     r[c].append(result)
    flagErr = False 
   return tuple([r, re])
 except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
  print(e)


def send_cfg_to_device(devices_list, config_commands):
 rr = {}
 for device in devices_list['routers']:
  r = send_config_command(device, config_commands, False)
  rr[device['ip']] = r
 return rr

if __name__ == "__main__":
 with open('devices.yaml', 'r') as f:
  y = yaml.load(f)
  rr = send_cfg_to_device(y, commands)
  print(rr)
