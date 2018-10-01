# -*- coding: utf-8 -*-
'''
Задание 18.1
add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах
В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными
Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import sqlite3
import glob
import yaml
import re
import create_db as db

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
sw = 'switches.yml'


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def write_data_to_db(connection, query, data):
    try:
        with connection:
            connection.executemany(query, data)
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)
        return False
    else:
        print('Write to sn success')
        return True

def get_all_from_db(connection, query):
    result = [row for row in connection.execute(query)]
    return result

def get_data_sw(sw):
 result = []
 with open(sw, 'r') as s:
  try:
    res = yaml.load(s)
  except yaml.YAMLError as e:
    print(e)
 for k0 in res.keys():
  for k1 in res[k0]:
   result.append(tuple([k1, res[k0][k1]]))
 return result

def get_data_dhcp(dhcp_snoop):
 row = []
 r = []
 m = re.search('(?P<host>\S+)_.+_', dhcp_snoop)
 if m:
  host = m.group('host')  
 with open(dhcp_snoop) as f:
  for l in f:
   match = re.search('(?P<mac>(?:\w{2}:){5}\w{2})\s+(?P<ip>(?:\d{1,3}.){3}\d{1,3})\s+\d+\s+\S+\s+(?P<vlan>\d+)\s+(?P<port>\S+)', l)
   if match:
    r = list(match.groups())
    r.append(host)
    row.append(tuple(r))
 return row

if __name__ == '__main__':
   data_dhcp_a = []
   data_sw = get_data_sw(sw)

   for dhcp_snoop_file in dhcp_snoop_files:
    data_dhcp = get_data_dhcp(dhcp_snoop_file)
    for t in data_dhcp:
     data_dhcp_a.append(t)


   if not db.is_db_exist():
    print('Db not exist, create first please')
    exit(1)

   c = create_connection(db_filename)
   q_insert_sw = 'INSERT into switches values (?, ?)'
   write_data_to_db(c, q_insert_sw, data_sw)

   q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?)'
   write_data_to_db(c, q_insert_dhcp, data_dhcp_a)
