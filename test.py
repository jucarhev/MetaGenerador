#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from src.Generator import *
obj_g = Generator()

array = [
	[0,"intedi","int(10)","Random 100,200", "dsfgs"],
	[1,"int","text","Random", "dsfgs"]
]

print(obj_g.create_mysql(array,5,'cliente'))