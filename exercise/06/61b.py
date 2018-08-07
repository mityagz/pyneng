#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 6.1
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

p = False
while True:
	ip=input("Enter ip addreess: ")
	ip = ip.split('.')
	c = "unused"
	if len(ip) != 4:
		print("Incorrect IPv4 address, try again")
		continue 

	i = 0
	while i < len(ip):
		if int(ip[i]) in range(0, 255):
			pass
		else:
			print("Incorrect IPv4 address, try again")
			p = True	
		i += 1
	if p :
	   p = False
	   continue

	if int(ip[0]) in range(1, 127):
   		c = 'A'
	elif int(ip[0]) in range(128, 191):
  		c = 'B'
	elif int(ip[0]) in range(192, 223):
   		c = 'C'
	elif int(ip[0]) in range(224, 239):
   		c = 'D'
	elif int(ip[0]) == 0:
   		c = 'UNA'
	elif int(ip[0]) == 255:
   		c = 'LB'
	else :
   		c = 'UNU'

	h = { 'A': 'unicast', 'B': 'unicast', 'C': 'unicast', 'D': 'multicast', 'UNA': 'unassigned', 'LB': 'local broadcast', 'UNU': 'unused' }
	print(h[c])
	break
