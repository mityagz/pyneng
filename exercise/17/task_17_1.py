#!/home/python/n/pyneng/bin/python

# -*- coding: utf-8 -*-
'''
Задание 17.1
В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате
Для выполнения задания нужно создать две функции.
Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"
Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает
Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.
Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv
В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime
В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.
Кроме того, создан список заголовков (headers), который должен быть записан в CSV.

result:
hostname,ios,image,uptime
r2,c7200-js-mz.124-4.T,C7200-JS-M 12.4(4)T,"45 days, 8 hours, 22 minutes"
r1,c1841-advipservicesk9-mz.124-15.T1.bin,C1841-ADVIPSERVICESK9-M 12.4(15)T1,"15 days, 8 hours, 32 minutes"
r3,c7200-js-mz.124-4.T,C7200-JS-M 12.4(4)T,"5 days, 18 hours, 2 minutes"
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

cvs_list = []

headers = ['hostname', 'ios', 'image', 'uptime']

cvs_list.append(headers)

for shfile in sh_version_files:
 with open(shfile) as f:
  h = re.search('sh_version_(\S+).txt', str(f))
  if h:
   hostname = h.group(1)
  for l in f:
   i = re.search('System image file is \"\S+:(\S+)\"', l.rstrip())
   if i:
    image = i.group(1)
   os = re.search('IOS Software,.*\((\S+)\), Version (\S+), \S+', l.rstrip())
   if os:
    ios = os.group(1) + ' ' + os.group(2)
   u = re.search('router uptime is (?P<ut>.*)', l.rstrip())
   if u:
    uptime = u.group('ut')
  cvs_list.append(list([hostname, image, ios, uptime]))



print(cvs_list)


with open('routers_inventory.csv', 'w') as f:
  writer = csv.writer(f)
  for d in cvs_list:
    writer.writerow(d)
