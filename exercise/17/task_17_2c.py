#!/home/python/n/pyneng/bin/python

# -*- coding: utf-8 -*-

import draw_network_graph as draw
import yaml

'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

topo = {}
topo1 = {}
topo_draw = {}

with open('topology.yaml') as f:
 topo = yaml.load(f)

for i in topo.keys():
 for i1 in topo[i].keys():
   for i2 in topo[i][i1].keys():
       k1 = tuple([i, i1])
       v1 = tuple([i2, topo[i][i1][i2]])
       try:
         if topo1[v1]:
          pass
       except:
          v1 = tuple([i2, topo[i][i1][i2]])
          topo1[k1] = v1

for e in topo.keys():
  neib = topo[e]
  for i in neib:
   d = tuple([e, i])
   for w in neib[i]:
    v = tuple([w, neib[i][w]])
    topo_draw[d] = v
   
draw.draw_topology(topo1)
