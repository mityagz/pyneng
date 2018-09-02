#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 12.2
Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.
Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.
Функция ожидает как аргумент список IP-адресов.
IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10
Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.
Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

import check_ip_addresses as ci
import ipaddress

l = ['127.0.0.3-127.0.0.7', '128.0.0.2-4', '127.0.0.3' , '128.0.0.1']
array_inp = []

def check_ip_availability(array_ip):
    for ip in array_ip: 
     if "-" in ip:
       l, r = ip.split("-") 
       if "." in r:
        ip_beg = int(l.split(".")[3])
        ip_end = int(r.split(".")[3])
        i = ip_beg
        while i <= ip_end:
         array_inp.append(".".join(l.split(".")[:3]) + "." + str(i))
         i += 1
       else:
        ip_beg = int(l.split(".")[3])
        ip_end = int(r)
        i = ip_beg
        while i <= ip_end:
         array_inp.append(".".join(l.split(".")[:3]) + "." + str(i))
         i += 1
     else:
      array_inp.append(ip)

    if len(array_inp) != 0:
     #print(ci.check_ip_addresses(array_inp)) 
     return ci.check_ip_addresses(array_inp)


if __name__ == '__main__':
 print(check_ip_availability(l))
