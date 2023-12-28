# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Sep 19 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import json

from src.Generator import *

###########################################################################
## Class Generador
###########################################################################

class Generador ( wx.Frame ):

	array_data_preview_generate = []

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador", pos = wx.DefaultPosition, size = wx.Size( 522,432 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		favicon = wx.Icon('src/icon/notebook.png',wx.BITMAP_TYPE_PNG, 16,16)
		self.SetIcon(favicon)
		self.SetSize((620,530))
		self.SetTitle("MetaGenerador")
		self.gui()
		self.Centre()
		self.Show()

		self.check_start()
		self.start_file_list()

	def gui(self):
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.tool_new_document = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/new-file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.AddSeparator()
		self.tool_database = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/database.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.AddSeparator()
		self.tool_export = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/export.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.AddSeparator()
		self.tool_preferences = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/settings.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.AddSeparator()
		self.tool_help = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/info.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.AddSeparator()
		self.tool_close = self.toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/power.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.toolbar.Realize()

		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Databases:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_comboBox1Choices = []
		self.cbo_databases = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer2.Add( self.cbo_databases, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tables:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_comboBox2Choices = []
		self.cbo_tables = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		bSizer2.Add( self.cbo_tables, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.btn_describe_table = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.btn_describe_table.SetBitmap( wx.Bitmap( u"src/icon/table.png", wx.BITMAP_TYPE_ANY ) )
		bSizer2.Add( self.btn_describe_table, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_comboBox3Choices = []
		self.cbo_columns = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		bSizer3.Add( self.cbo_columns, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"List:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer3.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_comboBox4Choices = []
		self.cbo_list = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.Size( 120,-1 ), m_comboBox4Choices, 0 )
		bSizer3.Add( self.cbo_list, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.txt_config = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer3.Add( self.txt_config, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.m_bpButton2.SetBitmap( wx.Bitmap( u"src/icon/info16x16.png", wx.BITMAP_TYPE_ANY ) )
		
		bSizer3.Add( self.m_bpButton2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		self.spin_number_items = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer4.Add( self.spin_number_items, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.btn_play = wx.Button( self, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_play, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.btn_clean = wx.Button( self, wx.ID_ANY, u"Clean", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_clean, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		self.list_preview = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.list_preview.InsertColumn(0, 'Num', width=50)
		self.list_preview.InsertColumn(1, 'Column', width=100)
		self.list_preview.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 80)
		self.list_preview.InsertColumn(3, 'Content', wx.LIST_FORMAT_RIGHT, 90)
		self.list_preview.InsertColumn(4, 'Example', wx.LIST_FORMAT_RIGHT, 220)
		bSizer5.Add( self.list_preview, 1, wx.ALL|wx.EXPAND, 5 )
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		self.SetSizer( bSizer1 )
		self.Layout()

		#ToolBar
		self.Bind(wx.EVT_TOOL, self.menu_file_newlist, self.tool_new_document)
		self.Bind(wx.EVT_TOOL, self.menu_edit_databases, self.tool_database)
		self.Bind(wx.EVT_TOOL, self.menu_file_export, self.tool_export)
		self.Bind(wx.EVT_TOOL, self.menu_file_close, self.tool_close)
		self.Bind(wx.EVT_TOOL, self.menu_edit_preferences, self.tool_preferences)
		self.Bind(wx.EVT_TOOL, self.OnAboutBox, self.tool_help)

		#Combos
		self.cbo_databases.Bind(wx.EVT_COMBOBOX, self.combo_change_databases)
		self.cbo_tables.Bind(wx.EVT_COMBOBOX, self.combo_change_tables)

		#Botones
		self.btn_play.Bind(wx.EVT_BUTTON,self.preview_info)
		self.btn_clean.Bind(wx.EVT_BUTTON,self.clean_info)
		self.btn_describe_table.Bind(wx.EVT_BUTTON,self.describe_table_database)

	def menu_file_newlist(self,event):
		conecta = newdocument_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()
		self.start_file_list()

	def menu_edit_databases(self,event):
		conecta = database_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()
		self.check_start()

	def menu_file_export(self,event):
		items = self.spin_number_items.GetValue()
		gen = Generator()
		if len(self.array_data_preview_generate) != 0:
			n = len(self.array_data_preview_generate)
			r = gen.create_mysql(self.array_data_preview_generate,items,self.cbo_tables.GetValue())
			conecta = export_dialog(None,r)
			conecta.ShowModal()
			conecta.Destroy()

	def menu_file_close(self, event):
		self.Destroy()

	def menu_edit_preferences(self,event):
		conecta = setting_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()

	def OnAboutBox(self,evt):
		conecta = about(None)
		conecta.ShowModal()
		conecta.Destroy()

	def combo_change_databases(self,evt):
		gen = Generator()
		self.cbo_tables.Clear()
		self.cbo_tables.SetValue('Ninguna')
		self.cbo_columns.SetValue('Ninguna')
		gen.check_connect()
		self.cbo_tables.AppendItems(gen.list_table_database(self.cbo_databases.GetValue()))

	def combo_change_tables(self,evt):
		try:
			gen = Generator()
			gen.check_connect()
			self.cbo_columns.Clear()
			self.cbo_columns.SetValue('Ninguna')
			self.cbo_columns.AppendItems(gen.columns_list(self.cbo_databases.GetValue(),self.cbo_tables.GetValue()))
		except Exception as e:
			print(e)

	def describe_table_database(self,event):
		if self.cbo_databases.GetValue() != 'Ninguna' or self.cbo_tables.GetValue() != 'Ninguna':
			conecta = description_table(None,self.cbo_databases.GetValue(),self.cbo_tables.GetValue())
			conecta.ShowModal()
			conecta.Destroy()
			self.check_start()

	def preview_info(self,event):
		if self.cbo_list.GetValue() == 'Date':
			if self.txt_config.GetValue() == 'r':
				wx.MessageBox("Date, no puede tener solo r, debe ser asi 1990,2000,r","Warning",wx.OK | wx.ICON_INFORMATION)

		gen = Generator()

		n = len(self.array_data_preview_generate)
		if self.cbo_list.GetValue() != 'Ninguna' or self.cbo_columns.GetValue() != 'Ninguna':
			columna = str(self.cbo_columns.GetValue()).split(' ')
			lista = self.cbo_list.GetValue()
			example = gen.examples(lista,self.txt_config.GetValue())
			array_preview = [n,columna[0],columna[1],lista + ' ' + self.txt_config.GetValue(),example]
			self.array_data_preview_generate.append(array_preview)

			self.list_preview.DeleteAllItems()

			idx = 0
			for ar in self.array_data_preview_generate:
				index = self.list_preview.InsertItem(idx, str(ar[0]))
				self.list_preview.SetItem(index, 1, str(ar[1]))
				self.list_preview.SetItem(index, 2, str(ar[2]))
				self.list_preview.SetItem(index, 3, str(ar[3]))
				self.list_preview.SetItem(index, 4, str(ar[4]))
				idx += 1

	def clean_info(self,event=None):
		self.list_preview.DeleteAllItems()
		self.array_data_preview_generate = []

	def start_file_list(self):
		gen = Generator()
		self.cbo_list.Clear()
		array1 = ['Ninguna','Email','Password','Date','Random','Feature','Telephone','Direction','Code','Secuencia']
		array2 = gen.list_files_diccionary()
		self.cbo_list.AppendItems(array1 + array2)

	def check_start(self):
		gen = Generator()
		if(gen.check_connect() != True):
			wx.MessageBox(str(gen.check_connect()), 'Error', wx.OK | wx.ICON_ERROR)
			self.cbo_databases.Clear()
			array1 = ['Ninguna']
			self.cbo_databases.AppendItems(array1)
		else:
			self.cbo_databases.Clear()
			array1 = ['Ninguna']
			array2 = gen.databases()
			self.cbo_databases.AppendItems(array1 + array2)


class newdocument_dialog ( wx.Dialog ):
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New document", pos = wx.DefaultPosition, size = wx.Size( 237,267 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt_newdocument = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,200 ), wx.TE_MULTILINE )
		bSizer14.Add( self.txt_newdocument, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_new_document = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.btn_new_document, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.btn_new_document.Bind(wx.EVT_BUTTON,self.save_config)
	
	def save_config( self ,evt):
		self.gen = Generator()
		try:
			dlg = wx.TextEntryDialog(self, 'Enter Name file','Name')
			if dlg.ShowModal() == wx.ID_OK:
				content = self.txt_newdocument.GetValue()
				self.gen.write_file(str(dlg.GetValue()) + '.txt', content)
				wx.MessageBox("Ok, Change", 'Ok', wx.OK | wx.ICON_INFORMATION)
			dlg.Destroy()
		except Exception as e:
			wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)

class database_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Database connection", pos = wx.DefaultPosition, size = wx.Size( 323,210 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"HostName:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txt_hostname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txt_hostname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"UserName:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txt_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txt_username, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer1.Add( self.txt_password, 0, wx.ALL, 5 )
		
		self.btn_save_connection = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn_save_connection, 0, wx.ALL, 5 )
		
		self.btn_test_connection = wx.Button( self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn_test_connection, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.gen = Generator()
		
		with open('src/config/config.json') as data:
			self.datos = json.load(data)

		self.txt_hostname.SetValue(self.datos['conn'][0])
		self.txt_username.SetValue(self.datos['conn'][1])
		self.txt_password.SetValue(self.datos['conn'][2])

		self.btn_save_connection.Bind(wx.EVT_BUTTON,self.save_config)
		self.btn_test_connection.Bind(wx.EVT_BUTTON,self.test_config)
	
	def save_config(self,evt):
		print(self.datos)
		try:
			self.datos['conn'][0] = self.txt_hostname.GetValue()
			self.datos['conn'][1] = self.txt_username.GetValue()
			self.datos['conn'][2] = self.txt_password.GetValue()

			with open('src/config/config.json', 'w') as jf: 
				json.dump(self.datos, jf)

			wx.MessageBox("Ok, Change", 'Ok', wx.OK | wx.ICON_INFORMATION)
		except Exception as e:
			wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)
		
	def test_config(self,evt):
		if self.gen.check_connect() == True:
			wx.MessageBox("Ok, Good", 'Ok', wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Fail", 'Error', wx.OK | wx.ICON_ERROR)

# pendiente
class export_dialog ( wx.Dialog ):
	
	def __init__( self, parent, content ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Export", pos = wx.DefaultPosition, size = wx.Size( 487,332 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt_export = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,300 ), wx.TE_MULTILINE )
		bSizer17.Add( self.txt_export, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )


		content = content.replace(',"");',');')
		content = content.replace(',,',',')
		self.txt_export.SetValue(content)

class description_table(wx.Dialog):
	def __init__( self,parent,database,table):
		wx.Dialog.__init__(self,parent=None,title='Describe Table',pos=wx.DefaultPosition,size=wx.Size(600,200))

		self.list = wx.ListCtrl(self, -1, pos=(10,170), size=(600,250),style=wx.LC_REPORT)
		self.list.InsertColumn(0, 'Field', width=100)
		self.list.InsertColumn(1, 'Type', width=100)
		self.list.InsertColumn(2, 'Null', wx.LIST_FORMAT_RIGHT, 70)
		self.list.InsertColumn(3, 'Key', wx.LIST_FORMAT_RIGHT, 70)
		self.list.InsertColumn(4, 'Default', wx.LIST_FORMAT_RIGHT, 70)
		self.list.InsertColumn(5, 'Extra', wx.LIST_FORMAT_RIGHT, 100)

		self.gen = Generator()
		self.gen.check_connect()
		rows = self.gen.query_model("SHOW COLUMNS FROM " + table,database)

		idx = 0
		for ar in rows:
			index = self.list.InsertItem(idx, str(ar[0]))
			self.list.SetItem(index, 1, str(ar[1]))
			self.list.SetItem(index, 2, str(ar[2]))
			self.list.SetItem(index, 3, str(ar[3]))
			self.list.SetItem(index, 4, str(ar[4]))
			self.list.SetItem(index, 5, str(ar[5]))
			idx += 1

class setting_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preferences", pos = wx.DefaultPosition, size = wx.Size( 285,189 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Exclude databases:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txt_exclude_databases = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer5.Add( self.txt_exclude_databases, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Exclude columns:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.txt_exclude_columns = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer5.Add( self.txt_exclude_columns, 0, wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_save_preferences = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btn_save_preferences, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.gen = Generator()
		with open("src/config/config.json") as archivo:
			self.datos = json.load(archivo)
		x = ''
		for dato in self.datos['dbexclude']:
			x = x+dato+','
		self.txt_exclude_databases.SetValue(x.rstrip(','))
		x = ''
		for dato in self.datos['tbexclude']:
			x = x+dato+','
		self.txt_exclude_columns.SetValue(x.rstrip(','))
		
		self.btn_save_preferences.Bind(wx.EVT_BUTTON,self.save_config)

	def save_config(self,evt):
		try:
			content = self.txt_exclude_databases.GetValue() + '\n' + self.txt_exclude_columns.GetValue()
			self.gen.write_file('preferences.txt', content ,'src/config/')
			wx.MessageBox("Ok, Change", 'Ok', wx.OK | wx.ICON_INFORMATION)
		except Exception as e:
			wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)

class about ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 450,439 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MetaGenerador", wx.DefaultPosition, wx.Size( 1000,50 ), wx.ALIGN_CENTRE )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		
		bSizer17.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"src/icon//notebook128x128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"MetaGenerador Generador de datos para mysql\n en formatos como MySQL escrito en wxpython ,\n python 3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText13.Wrap( -1 )
		bSizer17.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"juankarlos.0304@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer17.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"MetaGenerator", u"https://github.com/pacpac1992/MetaGenerador", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer17.Add( self.m_hyperlink1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Iconos de flaticons: www.flaticon.com \n Madebyoliver, Kirill Kazachek, Freepik \nLicence: Creative Commons BY 3.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer17.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )