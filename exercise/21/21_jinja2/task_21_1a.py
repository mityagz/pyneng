# -*- coding: utf-8 -*-
'''
Задание 21.1a

Дополнить функцию generate_cfg_from_template из задания 21.1:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

def generate_cfg_from_template(tmpl, vfile, **kw):
 TEMPLATE_DIR, template_file = os.path.split(tmpl)
 VARS_FILE = vfile

 env = Environment(loader = FileSystemLoader(TEMPLATE_DIR), **kw)
 template = env.get_template(template_file)

 vars_dict = yaml.load(open(VARS_FILE))
 return template.render(vars_dict)

if __name__ == '__main__':
 template = sys.argv[1]
 fvars = sys.argv[2]
 r = generate_cfg_from_template(template, fvars, trim_blocks=True, lstrip_blocks=True)
 #r = generate_cfg_from_template(template, fvars)
 print(r)
