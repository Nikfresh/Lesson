#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
m = sites['Moscow']
l = sites['London']
p = sites['Paris']
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
m_l=0.5
distances = dict()
m_l = ((m[0] - l[0])**2 + (m[1] - l[1])**2)** .5
m_p = ((m[0] - p[0])**2 + (m[1] - p[1])**2)** .5
l_p = ((l[0] - p[0])**2 + (l[1] - p[1])**2)** .5

distances['Moscow']={}
distances['Moscow']['London']=m_l
distances['Moscow']['Paris']=m_p

distances['London']={}
distances['London']['Moscow']=m_l
distances['London']['Paris']=l_p

distances['Paris']={}
distances['Paris']['Moscow']=m_p
distances['Paris']['London']=l_p


pprint(distances)




