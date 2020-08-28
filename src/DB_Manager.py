#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import mysql.connector

class DB_Manager( ):

	DB_HOST = 'localhost'
	DB_USER = 'root'
	DB_PASS = ''
	DB_NAME = ''
	
	def __init__(self,host,user,passw,db):
		self.DB_HOST = host
		self.DB_USER = user
		self.DB_PASS = passw
		self.DB_NAME = db

	def connection(self):
		try:
			self.connection = mysql.connector.connect(host=self.Host_Name,user=self.User_Name,password=self.Password,database=self.Database_Name)
			self.cursor = self.connection.cursor()
		except mysql.connector.Error as e:
			return e

	def close(self):
		self.connection.close()
		self.cursor.close()

	def execute_sql(self, sql, database):
		try:
			self.connection = mysql.connector.connect(host=self.Host_Name,user=self.User_Name,password=self.Password,database=database)
			self.cursor = self.connection.cursor()

			self.cursor.execute(sql)
			r = self.connection.commit()
			self.close()
			return r
		except mysql.connector.Error as e:
			return e

	def return_data(self,sql,database=''):
		try:
			self.connection = mysql.connector.connect(host=self.DB_HOST,user=self.DB_USER,password=self.DB_PASS, database=database)
			self.cursor = self.connection.cursor()
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			
			self.close()
			return data
		except mysql.connector.Error as e:
			return e

	def databases_list(self):
		try:
			array = self.return_data('SHOW DATABASES;','')
			databases = []
			for row in array:
				databases.append(row[0])
			return databases
		except Exception as e:
			return e

	def tables_list(self,database):
		self.DB_NAME = database
		try:
			if self.DB_NAME != '':
				array = self.return_data('SHOW TABLES;', database)
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
			result = self.return_data(query, database)
			columns = []
			for row in result:
				columns.append(row[0]+" "+row[1])
			return columns
		except Exception as e:
			return e

"""
con = Model('localhost','root','','')
print( con.databases_list() )
print( con.tables_list( 'test2' ) )
print( con.columns_list( 'test2' , 'test1' ) )
"""