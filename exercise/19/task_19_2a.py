# -*- coding: utf-8 -*-
'''
Задание 19.2a

Дополнить функцию send_config_commands из задания 19.2

Добавить аргумент verbose, который контролирует будет ли результат
выполнения команд выводится на стандартный поток вывода.

По умолчанию, результат должен выводиться.
'''

commands = [
    'set system location building NH', 'set system services netconf ssh'
]

import getpass
import sys
import yaml
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException


USER = input('Username: ')
PASSWORD = getpass.getpass()
DEVICES_IP = ['10.100.0.30', '10.100.0.31', '10.100.0.32']
USER = 'cisco'
PASSWORD = 'cisco5'

def send_config_command(device, command, verbose=True):
 r = {}
 DEVICE_PARAMS = device
 COMMAND = command
 print('Connection to device {}'.format(device['ip']))
 try:
  with ConnectHandler(**DEVICE_PARAMS) as ssh:
   ssh.config_mode()
   #for c in COMMAND:
   # result = ssh.send_command(c)
   # ssh.commit()	
   result = ssh.send_config_set(COMMAND, strip_command=verbose)
   ssh.commit()	
   if(verbose):
    print(result)
    
   r[device['ip']] = result
   return r
 except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
  print(e)

with open('devices.yaml', 'r') as f:
 y = yaml.load(f)


for device in y['routers']:
 r = send_config_command(device, commands, True)
