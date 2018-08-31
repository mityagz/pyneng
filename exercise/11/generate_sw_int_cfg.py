#!/home/python/n/pyneng/bin/python

import sw_int_templates as tmpl
import sw_data
from sw_data import sw1_fast_int

def generate_access_cfg(sw_dict):
    result = []
    for face, vlan  in sw_dict['access'].items():
        result.append(("interface FastEthernet {}".format(face)))
        for l in tmpl.access_template:
          if l.endswith("vlan"):
           result.append(' {} {}'.format(l, vlan))
          else:
           result.append(' {} '.format(l))
    return result

print('\n'.join(generate_access_cfg(sw_data.sw1_fast_int)))
print('\n'.join(generate_access_cfg(sw1_fast_int)))
