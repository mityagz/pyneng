import sqlite3
import re
import os
import yaml
from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days = 7)

def create_db(db, schema):
 print('Args: ', db, schema)
 print('Creating schema...')
 if is_db_exist(db):
  print('Db already exist')
  exit()
 with open(schema, 'r') as f:
  conn = sqlite3.connect(db)
  schema = f.read(); 
  conn.executescript(schema)
  conn.close()
 if is_db_exist(db):
  print('Done')
 else:
  print('Failure create db')

def add_data_switches(db_file, filename):
 print('Args: ', db_file, filename[0])
 data_sw = get_data_sw(filename[0])
 
 c = create_connection(db_file)
 q_insert_sw = 'INSERT into switches values (?, ?)'
 write_data_to_db(c, q_insert_sw, data_sw)
 c.close()

def add_data(db_file, filename):
 print('Args: ', db_file, filename)
 data_dhcp_a = []
 for dhcp_snoop_file in filename:
    data_dhcp = get_data_dhcp(dhcp_snoop_file)
    for t in data_dhcp:
     data_dhcp_a.append(t)

 print(data_dhcp_a)

 c = create_connection(db_file)
 r =  get_all_from_db(c, 'select * from dhcp')

 if not len(r):
 # remove old entries
   for d in r:
     if(str(d[6]) < str(week_ago)):
      print(d[0])
      q = 'delete from dhcp where mac = \'{}\''.format(d[0])
      get_all_from_db(c, q)
   c.commit()

   r =  get_all_from_db(c, 'select * from dhcp')

   if r:
   # db isn't empty
    for sw in data_dhcp_a:
     #q = 'update dhcp set active = 0 where switch = \'{}\' and mac = \'{}\''.format(sw[4], sw[0])
     q = 'update dhcp set active = 0'
     get_all_from_db(c, q)
    c.commit()

    for sw in data_dhcp_a:
     q = 'select mac from dhcp where mac = \'{}\''.format(sw[0])
     rr = get_all_from_db(c, q)
     if len(rr):
     # update exist data
      if sw[0] == rr[0][0]:
       q = 'update dhcp set ip = \'{}\', vlan = \'{}\', interface = \'{}\', active = 1 where mac = \'{}\''.format(sw[1], sw[2], sw[3], sw[0])
       get_all_from_db(c, q)
      else:
       q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1, \'{}\')'.format(now)
       write_data_to_db(c, q_insert_dhcp, sw)
     else:
     # insert missing data
       q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1, \'{}\')'.format(now)
       write_data_to_db(c, q_insert_dhcp, [ sw ])
       c.commit()
    c.commit()
   else:
   # db is empty, insert all
    print(now)
    print('empty')
    q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1, \'{}\')'.format(now)
    write_data_to_db(c, q_insert_dhcp, data_dhcp_a)

def get_data(db_file, key, value):
 print('Args: ', db_file, key, value)
 res = get_data_p(query(key, 1,  value), value, db_file)
 print_data(res, value, 1)
 res = get_data_p(query(key, 0,  value), value, db_file)
 print_data(res, value, 0)

def get_all_data(db_file):
 value = ''
 print('Args: ', db_file)
 res = get_data_p(query(), value, db_file)
 print_data(res, value, 1)
 res = get_data_p(query(False, 0, False), value, db_file)
 print_data(res, value, 0)


# private functions

def is_db_exist(db_filename):
 db_exists = os.path.exists(db_filename)
 if db_exists:
  return True

def create_connection(db_name):
 connection = sqlite3.connect(db_name)
 return connection

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

keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active', 'last_active']

def get_data_p(query, value, db_file):
 conn = sqlite3.connect(db_file)
 conn.row_factory = sqlite3.Row
 if value:
  result = conn.execute(query, (value,))
 else:
  result = conn.execute(query)
 return result

def print_data(result, value, a):
 if value:
  #print('\nDetailed information for host(s) with', key, value)
  pass
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

def get_all_from_db(connection, query):
 result = [row for row in connection.execute(query)]
 return result
