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

def print_data(result, value, a):
 if value:
  print('\nDetailed information for host(s) with', key, value)
 if a:
  print('\nActive value')
 else:
   print('\nInactive value')
 print('-' * 40)
 for row in result:
  for k in keys:
   print('{:10}: {}'.format(k, row[k]))
  print('-' * 40)

def query(key=False, a=1, value=False):
 if key:
  query = 'select * from dhcp where {} = ? and active = {}'.format( key, a )
 else:
  query = 'select * from dhcp where active = {}'.format(a)
 return query
 

if __name__ == '__main__':
 value = ''
 if len(sys.argv[1:]) == 2:
  key, value = sys.argv[1:]
  if not key in keys:
   print('parameter {} isn\'t support'.format(key))
   print('Try {}'.format(', '.join(keys)))
   exit(1)
  keys.remove(key)
  res = get_data(query(key, 1,  value), value)
  print_data(res, value, 1)
  res = get_data(query(key, 0,  value), value)
  print_data(res, value, 0)
 elif len(sys.argv[1:]) == 0:
  res = get_data(query(), value)
  print_data(res, value, 1)
  res = get_data(query(False, 0, False), value)
  print_data(res, value, 0)
 else:
  print('Too many args, need 0 or 2')
  exit(1)
