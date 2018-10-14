# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции, всегда будет передаваться только один из аргументов show, config, filename.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2
* filename - функция send_commands_from_file (ее надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt

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

def send_show_command(device, command):
 r = {}
 DEVICE_PARAMS = device
 COMMAND = command
 print('Connection to device {}'.format(device['ip']))
 with ConnectHandler(**DEVICE_PARAMS) as ssh:
  ssh.config_mode()
  result = ssh.send_command(COMMAND)
  r[device['ip']] = result
  return r


def send_cfg_to_device(devices_list, config_commands):
 rr = {}
 for device in devices_list['routers']:
  r = send_config_command(device, config_commands, False)
  rr[device['ip']] = r
 return rr

def send_commands_from_file(device, file_command):
 commands = []
 with open(file_command, 'r') as f:
  for line in f:
   commands.append(line.strip())
 f.close()
 r = send_config_command(device, commands)
 return r

def send_commands(device, show='', filename='', config=''):
 rr = {}
 if show:
  r =  send_show_command(device, show)
 elif filename:
  r =  send_commands_from_file(device, filename)
 elif config:
  r = send_config_command(device, config)
 rr[device['ip']] = r
 return rr

if __name__ == "__main__":
 with open('devices.yaml', 'r') as f:
  y = yaml.load(f)
 for device in y['routers']:
  #rr = send_commands(device, show='run show bgp summary')
  #rr = send_commands(device, config=correct_commands)
  rr = send_commands(device, filename='file_command')
  print(rr)
