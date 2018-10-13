# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

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

def send_config_command(device, command):
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
   result = ssh.send_config_set(COMMAND)
   ssh.commit()	
    
   r[device['ip']] = result
   return r
 except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
  print(e)

with open('devices.yaml', 'r') as f:
 y = yaml.load(f)


for device in y['routers']:
 r = send_config_command(device, commands)
 print(r)
