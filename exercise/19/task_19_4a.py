# -*- coding: utf-8 -*-
'''
Задание 19.4a

Дополнить функцию send_commands_to_devices таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе [subprocess](../../book/12_useful_modules/subprocess.md). Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands_to_devices.

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
import subprocess

def send_commands_to_devices(devices_list, show='', filename='', config=''):
 r = ss.send_commands(devices_list, show, filename, config)
 return r

def isPingable(ip):
 reply = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 if reply.returncode == 0:
  return True
 else:
  return False

if __name__ == "__main__":
 USER = input('Username: ')
 PASSWORD = getpass.getpass()
 rr = {}
 with open('devices2.yaml', 'r') as f:
  y = yaml.load(f)
 print(y)
 for device in y['routers']:
  device['username'] = USER
  device['password'] = PASSWORD
  if isPingable(device['ip']):
   rr = send_commands_to_devices(device, show='run show bgp summary')
   #rr = send_commands_to_devices(device, config=correct_commands)
   #rr = send_commands_to_devices(device, filename='file_command')
  else:
   print("Host {} is unavailable".format(device['ip']))
  if rr.keys():
   print(rr)
