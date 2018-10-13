# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''

command = 'run show interfaces brief'

import getpass
import sys
import yaml
from netmiko import ConnectHandler


USER = input('Username: ')
PASSWORD = getpass.getpass()
DEVICES_IP = ['10.100.0.30', '10.100.0.31', '10.100.0.32']
USER = 'cisco'
PASSWORD = 'cisco5'

#DEVICE_PARAMS = {
# 'device_type': 'juniper_junos',
# 'ip': IP,
# 'username': USER,
# 'password': PASSWORD
#}

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

with open('devices2.yaml', 'r') as f:
 y = yaml.load(f)

for r in y['routers']:
 r['username'] = USER
 r['password'] = PASSWORD


for device in y['routers']:
 r = send_show_command(device, command)
 print(r)
