# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2 и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"

В файле задания заготовлены команды с ошибками и без:
 junos:
set system arrr     
                    ^
syntax error.
--
set bgp           
             ^
syntax error.
--
set system 
                    ^
missing argument.
--
s
          ^
's' is ambiguous.
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
