# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_commands_threads, которая запускает функцию send_commands из задания 19.3 на разных устройствах в параллельных потоках.

Параметры функции send_commands_threads надо определить самостоятельно.
Должна быть возможность передавать параметры show, config, filename функции send_commands.

Функция send_commands_threads возвращает словарь с результатами выполнения команд на устройствах:

* ключ - IP устройства
* значение - вывод с выполнением команд

'''
import sys
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException


sys.path.insert(0, '../19/')
import task_19_3 as c


start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command):
    print(start_msg.format(datetime.now().time(), device_dict['ip']))
    if device_dict['ip'] == '10.100.0.30':
        time.sleep(10)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print(received_msg.format(datetime.now().time(), device_dict['ip']))
    return {device_dict['ip']: result}


def threads_conn(function, devices, limit, show = '', filename = '', config = ''):
    all_results = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [ executor.submit(function, device, show, filename, config) for device in devices ]
        for f in as_completed(future_ssh):
            try:
                result = f.result()
            except NetMikoAuthenticationException as e:
                print(e)
            else:
                all_results.update(result)
    return all_results

def send_commands_threads(devices, limit, show='', filename='', config=''):
  r = all_done = threads_conn(c.send_commands, devices['routers'], limit, show, filename, config)
  return r
  #pprint(all_done)


if __name__ == '__main__':
 devices = yaml.load(open('devices.yaml'))
 correct_commands = ['run show bgp summary', 'run show system uptime | match Curr']
 #result = send_commands_threads(devices, limit = 4, config=correct_commands)
 #result = send_commands_threads(devices, limit = 4, filename='file_command')
 result = send_commands_threads(devices, limit = 4, show='run show bgp summary')
 pprint(result)
