# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''


import sys
import task_22_5 as parse
import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
sys.path.insert(0, '../20/')
import netmiko_threads_submit_exception as conn
from concurrent.futures import ThreadPoolExecutor, as_completed


test_command = "sh ip int br"


def threads_conn(function, devices, limit=2, *command):
    all_results = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [ executor.submit(function, device, *command) for device in devices ]
        for f in as_completed(future_ssh):
            try:
                result = f.result()
            except NetMikoAuthenticationException as e:
                print(e)
            else:
                all_results.update(result)
    return all_results

def send_and_parse_command_parallel(devices, *c):
 with open(devices, 'r') as f:
  y = yaml.load(f)
 all_done = threads_conn(parse.send_and_parse_command, y['routers'], 2,  *c)
 return all_done

if __name__ == '__main__':
 command = 'run show route table inet.0'
 attributes = {'Command': 'run show int brief', 'Vendor': 'junos'}
 r = send_and_parse_command_parallel('devices2.yaml', attributes, 'index', 'templates', command, False)
 for k in r.keys():
  print(k, r[k])
