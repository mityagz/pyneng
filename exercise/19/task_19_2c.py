# -*- coding: utf-8 -*-
'''
Задание 19.2c

Переделать функцию send_config_commands из задания 19.2b

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды (значение по умолчанию)
* n - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками


Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить функцию на командах с ошибкой.

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

with open('devices.yaml', 'r') as f:
 y = yaml.load(f)


for device in y['routers']:
 r = send_config_command(device, commands, False)
 print(r[0])
 print(r[1])
