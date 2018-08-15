#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 9.2
Создать функцию, которая генерирует конфигурацию для trunk-портов.
Параметр trunk - это словарь trunk-портов.
Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):
    { 'FastEthernet0/1':[10,20],
      'FastEthernet0/2':[11,30],
      'FastEthernet0/4':[17] }
Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_template.
В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря trunk_dict.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]

    result = []

    for iface, vlan_list in trunk.items():
        result.append(("interface {}".format(iface)))
        for l in trunk_template:
            if l.endswith("allowed vlan"):
                l += " {}"
                result.append(l.format(",".join(str(v) for v in vlan_list)))
            else:
                result.append(l)

    return result

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

print(generate_trunk_config(trunk_dict))

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

    result = {}

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
        #result.append(("interface {}".format(iface)))
        #f = ("interface {}".format(iface))
        f = iface
        result[f] = []
        for l in access_template:
            if l.endswith("vlan"):
                l += " {}"
                result[f].append(l.format(vlan))
            else:
                result[f].append(l)
        if psecurity:
           for psec in port_security:
               result[f].append(psec)

    return result
 
access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

#print(generate_access_config(access_dict, True))
#print(generate_access_config(access_dict))
