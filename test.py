#!/usr/bin/python
# -*- coding: utf-8 -*-

# Test

"""
Aqui tus test, datos o ejemplos
"""

"""
San Luis Potosi Service Center
Carretera Central # 10700
Colonia La Raza
Soledad de Graciano Sanchez, SLP. CP 78120
Tel. (52) 444 854 54 98
"""

from src.Utils import *
from src.File_Manager import *

u = Utils()
#print(u.password_generate("30"))

"""Test para date_generate
print(u.date_generate("1980,2000","r"))
print(u.date_generate("1980,2000"))
print(u.date_generate("r"))
"""

fm = File_Manager()
fm.home_path()