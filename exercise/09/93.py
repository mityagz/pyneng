#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-
'''
Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

conf = []
result = {}
#result['trunk'] = {}
#result['access'] = {}

def get_int_vlan_map(cfg):
    with open(cfg) as f:
     for l in f:
       conf.append(l.rstrip())

    i = 0
    for cfgline in conf:
     i += 1
     if cfgline.startswith('interface Fast'):
       tp = ''
       vl = ''
       for lookforward in (conf[i:]):
         if not lookforward.startswith('!'):
            if lookforward.startswith(' switchport mode access'):
              tp = (lookforward.split(' '))[-1]
            elif lookforward.startswith(' switchport mode trunk'):
              tp = (lookforward.split(' '))[-1]
            elif "switchport access vlan" in lookforward:
              vl = (lookforward.split(' '))
            elif "switchport trunk allowed vlan" in lookforward:
              vl = (lookforward.split(' '))
         else:
          break
       if tp and tp not in result.keys():
          result[tp] = {}
          if cfgline and cfgline not in result[tp].keys():
           result[tp][cfgline] = []
       elif tp:
          result[tp][cfgline] = []

       if len(vl):
          result[tp][cfgline].append(vl[-1])


    return result

print(get_int_vlan_map('config_sw1.txt'))

'''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]

    result = {}

    for iface, vlan_list in trunk.items():
        result[iface] = []
        for l in trunk_template:
            if l.endswith("allowed vlan"):
                l += " {}"
                result[iface].append(l.format(",".join(str(v) for v in vlan_list)))
            else:
                result[iface].append(l)

    return result

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}
'''
