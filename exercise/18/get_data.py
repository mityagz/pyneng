# -*- coding: utf-8 -*-
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'


keys = ['mac', 'ip', 'vlan', 'interface', 'switch']

def get_data(query, value):
 conn = sqlite3.connect(db_filename)
 conn.row_factory = sqlite3.Row
 if value:
  result = conn.execute(query, (value,))
 else:
  result = conn.execute(query)
 return result

def print_data(result, value):
 if value:
  print('\nDetailed information for host(s) with', key, value)
 print('-' * 40)
 for row in result:
  for k in keys:
   print('{:10}: {}'.format(k, row[k]))
  print('-' * 40)

def query(key=False, value=False):
 if key:
  query = 'select * from dhcp where {} = ?'.format( key )
 else:
  query = 'select * from dhcp'
 return query
 

value = ''
if len(sys.argv[1:]) == 2:
 key, value = sys.argv[1:]
 keys.remove(key)
 res = get_data(query(key, value), value)
elif len(sys.argv[1:]) == 0:
 res = get_data(query(), value)
else:
 print('Too many args, need 0 or 2')
 exit(1)

print_data(res, value)
