#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from subprocess import PIPE, Popen
import os
import random
from os.path import expanduser

class File_Manager():
	
	def file_open(self,file,ruta=''):
		try:
			if ruta == '':
				ruta = 'diccionary/'
			f = open(ruta+file, "rw")
			archivo = f.read()
			f.close()
			return archivo
		except Exception as e:
			return e

	def write_file(self,file,content,ruta="diccionary/"):
		try:
			f = open(ruta+file, "w")
			archivo = f.write(content)
			f.close()
		except Exception as e:
			return 'Error'

	def delete_file(self,file):
		try:
			os.remove(os.getcwd() + '/diccionary/' + archivo + '.txt')
		except Exception as e:
			return 'Error'

	def new_file(self,file,content):
		try:
			f = open("diccionary/"+file, "w")
			archivo = f.write(content)
			f.close()
		except Exception as e:
			return 'Error'
	
	def file_lists(self):
		ruta = os.getcwd()
		nueva_ruta = os.chdir(ruta + '/diccionary')
		
		proceso = Popen(['ls'], stdout=PIPE, stderr=PIPE)
		error_encontrado = proceso.stderr.read()
		proceso.stderr.close()
		listado = proceso.stdout.read()
		proceso.stdout.close()
		ruta = os.chdir(ruta)

		if not error_encontrado:
			return listado
		else:
			return 'Error'

	"""
	================================================> Function since v1.0
	"""
	def home_path(self):
		home = expanduser("~")
		if os.path.exists(home+os.sep+'config'):
			print(home + os.sep+'config')
		else:
			ruta = os.mkdir(home+os.sep+'config',0777)
			os.mkdir(home+os.sep+'config'+os.sep+'diccionary',0777)
			os.mkdir(home+os.sep+'config'+os.sep+'preferences',0777)

			try:
				f = open(home+'/config'+os.sep+'preferences'+os.sep+'conn.txt', "w")
				archivo = f.write('localhost\nroot\nroot')
				f.close()
				d = open(home+''+os.sep+'config'+os.sep+'preferences'+os.sep+'preferences.txt', "w")
				db_column_exclude = 'information_schema,mysql,phpmyadmin,sys,performance_schema\nid,created_at,updated_at'
				archivo = d.write(db_column_exclude)
				d.close()
			except Exception as e:
				print 'Error'