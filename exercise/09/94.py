#!/home/python/n/pyneng/bin/python
# -*- coding: utf-8 -*-

'''
Задание 9.4
Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

result = {}
conf = []

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def config_to_dict(cfile):
    with open(cfile) as f:
     for l in f:
       if l.startswith('!') or ignore_command(l, ignore):
          pass
       else:
          conf.append(l.rstrip())
    for i in conf:
     if not i.startswith(' '):
      result[i] = []
      k = i
     else:
      result[k].append(i)
      print(i)

    return result

print(config_to_dict('config_sw1.txt'))