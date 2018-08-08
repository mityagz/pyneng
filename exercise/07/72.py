#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 7.2
Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту
Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.
Между строками не должно быть дополнительного символа перевода строки.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import sys

try:
    with open(sys.argv[1], 'r') as config:
        for l in config:
           if not l.rstrip().startswith("!"):
                print(l.rstrip())
except:
    print('No such file')
finally:
    config.close()


try:
    with open(sys.argv[1], 'r') as config:
        l = config.readlines()
        for i in l:
            if not i.startswith("!"):
                print(i.rstrip())
except:
    print('No such file')
finally:
    config.close()


