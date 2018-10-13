# -*- coding: utf-8 -*-
'''
Задание 19.1a

Переделать функцию send_show_command из задания 19.1 таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
command = 'run show interfaces brief'

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

def send_show_command(device, command):
 r = {}
 DEVICE_PARAMS = device
 COMMAND = command
 print('Connection to device {}'.format(device['ip']))
 try:
  with ConnectHandler(**DEVICE_PARAMS) as ssh:
   ssh.config_mode()
   result = ssh.send_command(COMMAND)
   r[device['ip']] = result
   return r
 except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
  print(e)

with open('devices.yaml', 'r') as f:
 y = yaml.load(f)


for device in y['routers']:
 r = send_show_command(device, command)
 print(r)
