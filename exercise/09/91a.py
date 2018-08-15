#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

import sys

'''
Задание 9.1a
Сделать копию скрипта задания 9.1.
Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение False
Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def generate_access_config(access, psecurity=False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    result = []

    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    for iface, vlan in access.items():
        result.append(("interface {}".format(iface)))
        for l in access_template:
            if l.endswith("vlan"):
                l += " {}"
                result.append(l.format(vlan))
            else:
                result.append(l)
        if psecurity:
           for psec in port_security:
               result.append(psec)

    return result
 
access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

#print(generate_access_config(access_dict, True))
print(generate_access_config(access_dict))
