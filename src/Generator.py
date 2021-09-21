#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from datetime import date
import hashlib

from src.Utils import *
from src.DB_Manager import *
from src.File_Manager import *

class Generator(File_Manager):
	
	def __init__(self):
		self.fm = File_Manager()

	def check_connect(self):
		file_check = self.file_open('conn.txt','src/config/')
		
		array_data_connect_server =  file_check.split("\n")
		
		if len(array_data_connect_server) == 2:
			array_data_connect_server.append('')

		self.db = DB_Manager(array_data_connect_server[0],array_data_connect_server[1],array_data_connect_server[2],'')
		test = str(self.db.return_data("SHOW DATABASES"))
		if isinstance( self.db.return_data("SHOW DATABASES"), list):
			return True
		else:
			return test

	def connection_server(self,database=''):
		file_check = self.file_open('conn.txt','src/config/')
		array_data_connect_server =  file_check.split("\n")
		self.db = DB_Manager(array_data_connect_server[0],array_data_connect_server[1],array_data_connect_server[2],database)
		return self.db

	def databases(self):
		file_preferences = self.file_open('preferences.txt','src/config/')
		array_file_preferences = file_preferences.split('\n')
		array_databases =  self.db.databases_list()
		for row in str(array_file_preferences[0]).split(','):
			#print(row)
			pass
			#array_databases.remove(row)
		return array_databases

	def list_files_diccionary(self):
		array1 = []
		for row in self.fm.file_lists():
			array1.append(row.replace('.txt','').capitalize())
		return array1

	def list_table_database(self,data):
		return self.db.tables_list(data)

	def columns_list(self,data,table):
		file_preferences = self.file_open('preferences.txt','src/config/')
		array_file_preferences = file_preferences.split('\n')
		array_columns_table =  self.db.columns_list(data,table)

		i = 0
		for column in array_columns_table:
			array_content_column = column.split(' ')
			for row in str(array_file_preferences[1]).split(','):
				if array_content_column[0] == row:
					array_columns_table.pop(i)
			i = i + 1

		print(array_columns_table)
		return array_columns_table

	def query_model(self,query,database):
		file_check = self.file_open('conn.txt','src/config/')
		array_data_connect_server =  file_check.split("\n")
		db_ = DB_Manager(array_data_connect_server[0],array_data_connect_server[1],array_data_connect_server[2],database)
		return db_.return_data(query,database)

	def examples(self,lista,option):
		u = Utils()
		return u.data_examples(lista,option)

	def create_info_to_array(self,content):
		array_data_content = ''
		array_content = ''
		for row in content:
			array_content = str(row[1])+'__'+str(row[2])+'__'+self.Generate_data_values(str(row[3]))
			array_data_content = array_data_content + array_content + ' == '
		return array_data_content

	def Generate_data_values(self,data):
		u = Utils()
		output = ""
		option = ""
		lista = ''
		if data.count(' ') == 1:
			array = data.split(' ')
			option = array[1]
			lista = array[0]
		elif data.count(' ') == 2:
			array = data.split(' ')
			option = str(array[1]) + " " + str(array[2])
			lista = array[0]
		else:
			lista = data


		if lista == "Email":
			output = u.generate_Email()
		elif lista == "Password":
			if option.count(',')  > 0:
				array = option.split(",")
				output = u.generate_password(array[0],array[1])
			else:
				output = u.generate_password(option)
		# Generate random, integer or float
		elif lista == "Code":
			output = u.generate_Code(option)
		elif lista == "Random":
			if option == "":
				output = str(random.randint(1,1000))
			elif option.count(",") > 0 and option.count("d") == 0:
				array = option.split(",")
				output = str(random.randint(int(array[0]),int(array[1])))
			elif option.count("d") > 0:
				if option.count(",") == 0:
					output = str(round(random.uniform(0.0, 10.9)))
				else:
					array = option.split(",")
					a = float(array[0])
					b = float(array[1])
					output = str(round(random.uniform(a,b),1))
			else:
				output = str(random.randint(1,1000))
		elif lista == "Feature":
			if option == "":
				output = random.choice(['item1','item2','item3','item4','item5'])
			else:
				output = random.choice(option.split(','))
		elif lista == "Telephone":
			if option == "":
				output = str(random.randint(4400000001,9999999999))
			elif option == "home":
				output = "01 "+str(random.randint(44000001,99999999))
			else:
				output = "["+option+"]"
		elif lista == "Direction":
			output = "Calle " + str(random.choice(u.consonantes)) + ", numero " + str(random.randint(1,1000))
			output = output + ", manzana " + str(random.randint(1,500))
		elif lista == "Date":
			if option.count(' ')>0:
				array_option = option.split(' ')
				output = u.generate_Date(array_option[0],True)
			elif option.count('r')>0 and option.count(' ') == 0 and option.count('ri') ==0:
				output = u.generate_Date('',True)
			elif option.count(' ') == 0 and option.count('ri') == 1:
				output = u.generate_Date('',True,'-,')
			elif option == '':
				output = u.generate_Date()
			else:
				output = u.generate_Date(option)
		elif lista == "Ninguna":
			output = ""
		elif lista == "Secuencia":
			output = "/secuencia/"
		else:
			if lista != '':
				if option == '':
					output = u.return_content_file(lista)
					if output.count(' ') > 0:
						array = str(u.return_content_file(lista)).split(' ')
						output = array[0]
				else:
					n = 0
					if option.isdigit():
						n = int(option)
						for x in xrange(0,n):
							output =  output + ' ' + u.return_content_file(lista)
					elif option == 'r':
						output = u.return_content_file(lista)
						if output.count(' ') > 0:
							array = str(u.return_content_file(lista)).split(' ')
							output = str(array[0]) + '_,_' +  str(array[1])
					elif option == 'ri':
						output = u.return_content_file(lista)
						if output.count(' ') > 0:
							array = str(u.return_content_file(lista)).split(' ')
							output = str(array[0]) + '-,' +  str(array[1])
			else:
				output = ''
		return output

	def create_mysql(self,content,items,table):
		data = ''
		for x in range(0,items):
			columns = ''
			values = ''
			sql = 'INSERT INTO ' + table + '('
			output = self.create_info_to_array(content)
			output = output.rstrip(' == ')
			array = output.split(' == ')
			for row in array:
				array2 = row.split('__')
				
				columns = columns + str(array2[0]) + ','
				if str(array2[1]).count("int") == 0 and str(array2[1]).count("double") == 0:
					if str(array2[2]).count('_,_'):
						values = values + '"' + str(array2[2]).replace('_,_','","') + '",'
						values = values.replace('/secuencia/','"'+str(x+1)+'"')
					elif str(array2[2]).count('-,'):
						values = values + '"' + str(array2[2]).replace('-,','",') + ','
						values = values.replace('/secuencia/','"'+str(x+1)+'"')
					else:
						values = values + '"' + str(array2[2]) + '",'
						values = values.replace('/secuencia/','"'+str(x+1)+'"')
				else:
					values = values + str(array2[2]) + ','
					values = values.replace('/secuencia/',str(x+1))

			sql = sql + columns.rstrip(',') + ') VALUES (' + values.rstrip(',') + ');'
			data = data + sql + '\n'
			data = data.replace(',"",',',')
			data = data.replace('""','"')

		return data
		