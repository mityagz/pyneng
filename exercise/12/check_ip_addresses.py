#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 12.1
Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.
Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess

def check_ip_addresses(array_ip):
  alive = []
  dead = []
  for ip in array_ip:
    reply = subprocess.run(['ping', '-c', '3', '-n', ip],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
      alive.append(ip)
    else:
      dead.append(ip)

  return(alive, dead)
     
l = ['127.0.0.1', '128.0.0.2', '127.0.0.2' , '128.0.0.1']


if __name__ == '__main__':
 print(check_ip_addresses(l))
