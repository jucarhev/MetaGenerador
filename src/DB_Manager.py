#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, MySQLdb

class DB_Manager():
	""" Class DB_Manager
		Connection to database mysql
	"""

	DB_HOST = 'localhost'
	DB_USER = 'root'
	DB_PASS = ''
	DB_NAME = ''
	
	def __init__(self,host,user,passw,db):
		self.DB_HOST = host
		self.DB_USER = user
		self.DB_PASS = passw
		self.DB_NAME = db

	def run_query(self,query=''):
		try:
			datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]
			conn = MySQLdb.connect(*datos)
			cursor = conn.cursor()
			cursor.execute(query)
			if query.upper().startswith('SELECT'):
				data = cursor.fetchall()
			elif query.upper().startswith('SHOW'):
				data = cursor.fetchall()
			else:
				conn.commit()
				data = None
			
			cursor.close()
			conn.close()

			return data
		except Exception as e:
			return 'Error: ' + str(e)

	def databases_list(self):
		try:
			array = self.run_query('SHOW DATABASES;')
			databases = []
			for row in array:
				databases.append(row[0])
			return databases
		except Exception as e:
			return False

	def tables_list(self,database):
		self.DB_NAME = database
		try:
			if self.DB_NAME != '':
				array = self.run_query('SHOW TABLES;')
				databases = []
				for row in array:
					databases.append(row[0])
				return databases
			else:
				return []
		except Exception as e:
			return e

	def columns_list(self,database,table):
		self.DB_NAME = database
		try:
			query = "show columns from " + table
			result = self.run_query(query)
			columns = []
			for row in result:
				columns.append(row[0]+" "+row[1])
			return columns
		except Exception as e:
			return e