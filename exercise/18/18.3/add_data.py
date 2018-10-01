# -*- coding: utf-8 -*-

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
       q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1)'
       write_data_to_db(c, q_insert_dhcp, sw)
     else:
     # insert missing data
       q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1)'
       write_data_to_db(c, q_insert_dhcp, [ sw ])
       c.commit()
    c.commit()
   else:
   # db is empty, insert all
    q_insert_sw = 'INSERT into switches values (?, ?)'
    write_data_to_db(c, q_insert_sw, data_sw)
    q_insert_dhcp = 'INSERT into dhcp values (?, ?, ?, ?, ?, 1)'
    write_data_to_db(c, q_insert_dhcp, data_dhcp_a)
