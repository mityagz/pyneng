import sqlite3
import re
import os

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
result = []


data_filename = 'dhcp_snooping.txt'
db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'


with open('dhcp_snooping.txt', 'r') as data:
 for line in data:
  m = regex.search(line)
  if m:
   result.append(m.groups())

db_exists = os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

if not db_exists:
 print('Creating schema...')
 with open('dhcp_snooping_schema.sql', 'r') as f:
  schema = f.read(); 
 conn.executescript(schema)
 print('Done')
else:
 print('Database exists, assume dhcp table does, too.')

print('Inserting DHCP Snooping data')

query = 'insert into dhcp (mac, ip, vlan, interface) values (?, ?, ?, ?)'

for row in result:
  try:
   with conn:
    print(row)
    conn.execute(query, row)
  except sqlite3.IntegrityError as e:
   print('Error occured: ', e)

conn.close()
   
                       
