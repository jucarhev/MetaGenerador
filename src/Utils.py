#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from datetime import date
import hashlib

from src.File_Manager import *

class Utils():	
	
	extension = ['@gmail.com','@hotmail.com','@yahoo.com','@company.com']
	extras = ['0','1','2','3','4','5','6','7','8','9']
	consonantes = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
	vocales = ['A','E','I','O','U']

	def generate_Email(self):
		mail = ''
		for x in range(1,4):
			mail = mail + random.choice(self.vocales) + random.choice(self.consonantes)
		
		for x in range(0,2):
			mail = mail + random.choice(self.extras) + random.choice(self.extras)

		mail = mail + random.choice(self.extension)

		return mail

	def generate_Code(self,num="12"):
		code = ""
		
		if num == "":
			num = "12"

		for x in range(0,int(num)):
			for rango in range(1,3):
				if rango == 1:
					code = code + random.choice(self.extras)
				elif rango == 2:
					code = code + random.choice(self.consonantes)
				elif rango == 3:
					code = code + random.choice(self.vocales)
		return code;

	def generate_password(self,num="",cifrado=""):
		if num == "":
			num = "8"

		n = int(num) / 2
		password = ''

		for x in range(0,n):
			password = password + random.choice(self.consonantes) + random.choice(self.vocales)
		
		if cifrado == "":
			return password
		elif cifrado == "sha1":
			return hashlib.sha1('secret').hexdigest()
		elif cifrado == "md5":
			return hashlib.md5('secret').hexdigest()

	def generate_Date(self,rango = "1990,2000", dif = False,inte = ''):
		try:
			mes = random.randint(1,12)
			dia = random.randint(1,31)

			if mes == 4 or mes == 6 or mes == 8 or mes == 10:
				if dia == 31:
					dia = 30

			elif mes == 2:
				if dia > 28:
					dia = 28

			array = rango.split(",")

			inicio = int(array[0])
			fin = int(array[1])

			if inicio < fin:
				anio = random.randint(inicio,fin)
			else:
				anio = random.randint(1990,2000)

			year_now = date.today().year

			if dif == False:
				return str(anio) + "-" + str(mes) + "-" + str(dia)
			else:
				if inte == '':
					return str(anio) + "-" + str(mes) + "-" + str(dia) + "_,_" + str(year_now - anio)
				else:
					return str(anio) + "-" + str(mes) + "-" + str(dia) + "-," + str(year_now - anio)

		except Exception as e:
			if dif == False:
				return "1990-02-20"
			else:
				return "1990-02-20_,_" + str(date.today().year - 1990)

	def data_examples(self,lista,option=""):
		salida = " "
		if lista == "Email":
			salida = self.generate_Email()
		elif lista == "Password":
			if option.count(',')  > 0:
				array = option.split(",")
				salida = self.generate_password(array[0],array[1])
			else:
				salida = self.generate_password(option)
		elif lista == "Code":
			salida = "WE34EWR54H56H"
		elif lista == "Random":
			if option == "":
				salida = str(random.randint(1,1000))
			elif option.count(",") > 0:
				array = option.split(",")
				salida = str(random.randint(int(array[0]),int(array[1])))
			else:
				salida = str(random.randint(1,1000))
		elif lista == "Secuencia":
			salida = "Secuencia"
		elif lista == "Feature":
			if option == "":
				salida = "[item1,item2,item3,item4,item5]"
			else:
				salida = "["+option+"]"
		elif lista == "Telephone":
			if option == "":
				salida = str(random.randint(4400000001,9999999999))
			elif option == "home":
				salida = "01 "+str(random.randint(44000001,99999999))
			else:
				salida = "["+option+"]"
		elif lista == "Direction":
			salida = "Calle " + str(random.choice(self.consonantes)) + ", numero " + str(random.randint(1,1000))
			salida = salida + ", manzana " + str(random.randint(1,500))
		elif lista == "Date":
			salida = "15-10-2009"
		elif lista == "Ninguna":
			salida = ""
		else:
			salida = self.return_content_file(lista)
			if salida.count(' ') > 0:
				array = str(self.return_content_file(lista)).split(' ')
				salida = array[0]
		return salida

	def return_content_file(self, file):
		fm = File_Manager()
		array_content_file = str(fm.file_open(file+'.txt')).split('\n')
		dato = random.choice(array_content_file)
		return dato

