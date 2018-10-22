# -*- coding: utf-8 -*-
'''
Задание 21.3a

Измените шаблон templates/ospf.txt таким образом, чтобы для перечисленных переменных
были указаны значения по умолчанию, которые используются в том случае,
если переменная не задана.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf2.yml,
с помощью функции generate_cfg_from_template из задания 21.1-21.1c.
Не копируйте код функции.
'''


import task_21_1c as gen
import sys

if __name__ == '__main__':
 template = sys.argv[1]
 fvars = sys.argv[2]
 r = gen.generate_cfg_from_template(template, fvars, trim_blocks=True, lstrip_blocks=True)
 #r = gen.generate_cfg_from_template(template, fvars, trim_blocks=False, lstrip_blocks=False)
 print(r)
