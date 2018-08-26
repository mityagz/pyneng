#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 9.4a
Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt
Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100
Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.
Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками
Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.
На примере interface Ethernet0/3.100:
{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)

ignore = ['duplex', 'alias', 'Current configuration']

result = {}
conf = []

def level(conf):
 deep1 = 0
 deep2 = 0
 deep3 = 0
 level = 0
 for i in conf:
   if i.startswith('  '):
    deep3 = 1
    deep2 = 0
    level = 3
   elif i.startswith(' ') and not deep3:
    deep2 = 1
    level = 2

 return level    

def config_to_dict(cfile):
    with open(cfile) as f:
     for l in f:
       if '!' in l  or check_ignore(l, ignore):
          pass
       else:
          conf.append(l.rstrip())

    l = level(conf)
    j = 0

    for i in conf:
     if not i.startswith(' ') and l == 2:
      result[i] = []
      k = i
     elif i.startswith(' ') and l == 2:
      result[k].append(i)
     if not i.startswith(' ') and l == 3:
      result[i] = {}
      k = i
     elif i.startswith(' ') and not i.startswith('  ') and l == 3:
      result[k][i] = []
      j = i
     elif i.startswith('  ') and l == 3:
      result[k][j].append(i)

    return result


res  = config_to_dict('config_r1.txt')
#res  = config_to_dict('config_sw1.txt')
print(res)
l = level(conf)
print(l)
