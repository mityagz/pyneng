# -*- coding: utf-8 -*-
"""
Задание 18.1
create_db.py
* сюда должна быть вынесена функциональность по созданию БД:
 * должна выполняться проверка наличия файла БД
 * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
   должна быть создана БД (БД отличается от примера в разделе)
В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches
Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
"""

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

import sqlite3
import re
import os

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
result = []


data_filename = 'dhcp_snooping.txt'
db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
 

def is_db_exist():
 db_exists = os.path.exists(db_filename)
 if db_exists:
  return True

def create_db(db, schema):
 print('Creating schema...')
 with open(schema, 'r') as f:
  conn = sqlite3.connect(db)
  schema = f.read(); 
  conn.executescript(schema)
  conn.close()
 if is_db_exist():
  print('Done')
 else:
  print('Failure create db')



if __name__ == '__main__':
 if not is_db_exist():
  create_db(db_filename, schema_filename)
 else:
  print('Database exists, assume dhcp table does, too.')

 
