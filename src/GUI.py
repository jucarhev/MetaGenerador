# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## Update by juankarlos.0304@gmail.com
###########################################################################

import wx
import wx.xrc
import wx.aui

# Import class
from Generator import *
from Dialogs import *
from Tabs import *

###########################################################################
## Class GUI
###########################################################################

class GUI ( wx.Frame ):
	
	array_data_preview_generate = []

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador", pos = wx.DefaultPosition, size = wx.Size( 522,432 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		favicon = wx.Icon('src/icon/notebook.png',wx.BITMAP_TYPE_PNG, 16,16)
		self.SetIcon(favicon)
		self.gui()
		self.SetSize((690,530))
		self.SetTitle("MetaGenerador")
		self.Centre()
		self.Show()

		self.check_start()
		self.start_file_list()
		
	def gui(self):
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.SetForegroundColour( wx.Colour( 000, 000, 000 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		#-------------> start toolbar
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.tool_new_document = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/new-file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL,u"Create new list",wx.EmptyString, None ) 
		self.tool_edit_document = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/listas.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL,u"Create new list",wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_database = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/database.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_export = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/export.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_preferences = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/settings.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_help = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/info.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_close = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/power.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.Realize() 

		#-------------> end toolbar
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		#-------------> start firts row
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Databases:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer5.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cbo_databasesChoices = []
		self.cbo_databases = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, cbo_databasesChoices, 0 )
		bSizer5.Add( self.cbo_databases, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Tables:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer5.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cbo_tablesChoices = []
		self.cbo_tables = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, cbo_tablesChoices, 0 )
		bSizer5.Add( self.cbo_tables, 0, wx.ALL, 5 )
		
		self.btn_describe_table = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"src/icon/table.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer5.Add( self.btn_describe_table, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		

		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		#-------------> end firts row
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		#-------------> start second row

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer6.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cbo_columnsChoices = []
		self.cbo_columns = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, cbo_columnsChoices, 0 )
		bSizer6.Add( self.cbo_columns, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"List:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer6.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cbo_listChoices = []
		self.cbo_list = wx.ComboBox( self, wx.ID_ANY, u"Ninguna", wx.DefaultPosition, wx.DefaultSize, cbo_listChoices, 0 )
		bSizer6.Add( self.cbo_list, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txt_config = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (200,30), 0 )
		bSizer6.Add( self.txt_config, 0, wx.ALL, 5 )
		
		self.btn_help_list = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"src/icon/info16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer6.Add( self.btn_help_list, 0, wx.ALL, 5 )

		self.btn_play = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_play, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )

		#-------------> end second row

		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		#-------------> list- table
		self.list_preview = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.list_preview.InsertColumn(0, 'Num', width=50)
		self.list_preview.InsertColumn(1, 'Column', width=100)
		self.list_preview.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 80)
		self.list_preview.InsertColumn(3, 'Content', wx.LIST_FORMAT_RIGHT, 90)
		self.list_preview.InsertColumn(4, 'Example', wx.LIST_FORMAT_RIGHT, 220)
		bSizer8.Add( self.list_preview, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4.Add( bSizer8, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.spin_number_items = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 500, 1 )
		bSizer9.Add( self.spin_number_items, 0, wx.ALL, 5 )

		combo_tipoChoices = [u"MySQL",u"MongoDB",u"Oracle",u"SQLServer",u"JSon",u"XML"]
		self.combo_tipo = wx.ComboBox( self, wx.ID_ANY, u"MySQL", wx.DefaultPosition, wx.DefaultSize, combo_tipoChoices, 0 )
		bSizer9.Add( self.combo_tipo, 0, wx.ALL, 5 )

		self.btn_generate_data = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn_generate_data, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"\t\t", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer9.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.btn_insert_into = wx.Button( self, wx.ID_ANY, u"Insert into", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn_insert_into, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"\t\t", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer9.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.btn_view_table_content = wx.Button( self, wx.ID_ANY, u"Select *", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn_view_table_content, 0, wx.ALL, 5 )

		bSizer4.Add( bSizer9, 0, wx.EXPAND, 5 )

		#-------------> start Tab
		self.tabs = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		bSizer4.Add( self.tabs, 1, wx.EXPAND |wx.ALL, 5 )
		
		#-------------> end Tab
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		#-------------> Events ToolBar
		self.Bind(wx.EVT_TOOL, self.menu_file_newlist, self.tool_new_document)
		self.Bind(wx.EVT_TOOL, self.menu_edit_databases, self.tool_database)
		self.Bind(wx.EVT_TOOL, self.menu_file_export, self.tool_export)
		self.Bind(wx.EVT_TOOL, self.menu_edit_preferences, self.tool_preferences)
		self.Bind(wx.EVT_TOOL, self.OnAboutBox, self.tool_help)
		self.Bind(wx.EVT_TOOL, self.menu_file_close, self.tool_close)

		#-------------> Events Buttons
		self.btn_play.Bind(wx.EVT_BUTTON,self.preview_info)
		#self.btn_clean.Bind(wx.EVT_BUTTON,self.clean_info)
		self.btn_describe_table.Bind(wx.EVT_BUTTON,self.describe_table_database)
		self.btn_help_list.Bind(wx.EVT_BUTTON,self.help_list_description)
		self.btn_view_table_content.Bind(wx.EVT_BUTTON,self.select_table)
		self.btn_generate_data.Bind(wx.EVT_BUTTON,self.tab_generate_data)
		self.btn_insert_into.Bind(wx.EVT_BUTTON,self.insert_into)

		#-------------> Events Combos
		self.cbo_databases.Bind(wx.EVT_COMBOBOX, self.combo_change_databases)
		self.cbo_tables.Bind(wx.EVT_COMBOBOX, self.combo_change_tables)
		self.cbo_list.Bind(wx.EVT_COMBOBOX, self.clean_options)

		#-------------> Events list
		self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onListBox, self.list_preview)
	
	#####################################
	#			Methods Menu, toolbar 			
	#####################################
	def menu_file_close(self, event):
		self.Destroy()

	def menu_file_export(self,event):
		items = self.spin_number_items.GetValue()
		gen = Generator()
		if len(self.array_data_preview_generate) != 0:
			n = len(self.array_data_preview_generate)
			r = gen.create_mysql(self.array_data_preview_generate,items,self.cbo_tables.GetValue())
			conecta = export_dialog(None,r)
			conecta.ShowModal()
			conecta.Destroy()

	def menu_file_newlist(self,event):
		conecta = newdocument_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()
		self.start_file_list()

	def menu_edit_preferences(self,event):
		conecta = setting_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()

	def menu_edit_databases(self,event):
		conecta = database_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()
		self.check_start()

	def menu_edit_menulist(self,event):
		conecta = list_dialog(None)
		conecta.ShowModal()
		conecta.Destroy()
		self.check_start()

	######################################
	def onListBox(self,evt):
		self.popupmenu = wx.Menu()
		for text in ['Delete','Delete All']:
			item = self.popupmenu.Append(-1, text)
			self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
		self.list_preview.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
		

		index = self.list_preview.GetFirstSelected()
		if index == -1:
			print("tNone")
		while index != -1:
			item = self.list_preview.GetItem(index)
			self.item_list_selected = item.GetText()
			index = self.list_preview.GetNextSelected(index)

	def OnShowPopup(self, event):
		pos = event.GetPosition()
		pos = self.ScreenToClient(pos)
		self.PopupMenu(self.popupmenu, pos)

	def OnPopupItemSelected(self, event):
		item = self.popupmenu.FindItemById(event.GetId())
		text = item.GetText()
		if text == "Delete":
			index = self.item_list_selected
			self.array_data_preview_generate.pop(int(index))
			self.edit_array_()
			self.llenar_vista_previa()
		elif text == "Delete All":
			self.clean_info()

	def edit_array_(self):
		i = 0
		for row in self.array_data_preview_generate:
			row[0] = i
			i = i + 1

	#####################################
	#		Buttons Methods
	#####################################
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

			for ar in self.array_data_preview_generate:
				index = self.list_preview.InsertStringItem(sys.maxint, str(ar[0]))
				self.list_preview.SetStringItem(index, 1, str(ar[1]))
				self.list_preview.SetStringItem(index, 2, str(ar[2]))
				self.list_preview.SetStringItem(index, 3, str(ar[3]))
				self.list_preview.SetStringItem(index, 4, str(ar[4]))

	def llenar_vista_previa(self):
		self.list_preview.DeleteAllItems()

		for ar in self.array_data_preview_generate:
			index = self.list_preview.InsertStringItem(sys.maxint, str(ar[0]))
			self.list_preview.SetStringItem(index, 1, str(ar[1]))
			self.list_preview.SetStringItem(index, 2, str(ar[2]))
			self.list_preview.SetStringItem(index, 3, str(ar[3]))
			self.list_preview.SetStringItem(index, 4, str(ar[4]))

	def clean_info(self,event=None):
		self.list_preview.DeleteAllItems()
		self.array_data_preview_generate = []

	def describe_table_database(self,event):
		if self.cbo_databases.GetValue() != 'Ninguna' or self.cbo_tables.GetValue() != 'Ninguna':
			conecta = description_table(None,self.cbo_databases.GetValue(),self.cbo_tables.GetValue())
			conecta.ShowModal()
			conecta.Destroy()
			self.check_start()

	def help_list_description(self,event):
		if self.cbo_list.GetValue() != 'Ninguna':
			if self.cbo_list.GetValue() == 'Email':
				wx.MessageBox('Return email, Example: EWEXAN1458@company.com','Email', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Password':
				content = 'puede usarse sha1 o md5, en ambos casos la contraseña es "secret"';
				content = content + '\nParams: None 	Return string(8) 	= YUCUXUPI'
				content = content + '\nParams: 10 	Return string(10) 	= YUCUXUPISE'
				content = content + '\nParams: 10,sha1 	Return string(10) 	= sha1(secret)'
				wx.MessageBox('Return password, Example: '+content,'Password', wx.OK | wx.ICON_INFORMATION)

			elif self.cbo_list.GetValue() == 'Random':
				content = '\nParams: None 		Return random(0,100) 		= 5\n'
				content = content +'Params: 0,200 		Return random(0,200) 		= 123\n'
				content = content +'Params: 0,200,d 		Return random(0.0,200.0) 	= 123.5'
				wx.MessageBox('Return Random, Example: '+content,'Random', wx.OK | wx.ICON_INFORMATION)
			
			elif self.cbo_list.GetValue() == 'Custom':
				content = '\nParams example: one,two,three'
				wx.MessageBox('Return Custom value of the array, Example: '+content,'Custom', wx.OK | wx.ICON_INFORMATION)
			
			elif self.cbo_list.GetValue() == 'Telephone':
				content = '\nParams None / Home(01 ) '
				wx.MessageBox('Return Telephone value of the array, Example: '+content,'Telephone', wx.OK | wx.ICON_INFORMATION)
			
			elif self.cbo_list.GetValue() == 'Direction':
				content = '\nParams None / Home(01 ) '
				wx.MessageBox('Return Direction value of the array, Example: '+content,'Direction', wx.OK | wx.ICON_INFORMATION)
			
			elif self.cbo_list.GetValue() == 'Date':
				content = '\nParams None return 1990-02-3'
				content = '\nParams r (Return differents with year) '
				wx.MessageBox('Return Date value of the array, Example: '+content,'Date', wx.OK | wx.ICON_INFORMATION)

	#####################################
	#		Combos Methods
	#####################################
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
			print e

	def clean_options(self,evt):
		self.txt_config.SetValue('')
	
	#####################################
	# 		Methods Utils
	#####################################
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

	def start_file_list(self):
		gen = Generator()
		self.cbo_list.Clear()
		array1 = ['Ninguna','Email','Password','Date','Random','Custom','Telephone','Direction','Code','Secuencia']
		array2 = gen.list_files_diccionary()
		self.cbo_list.AppendItems(array1 + array2)

	def OnAboutBox(self,evt):
		conecta = about(None)
		conecta.ShowModal()
		conecta.Destroy()
	
	def select_table(self,evt=None):
		if self.cbo_databases.GetValue() != 'Ninguna' and self.cbo_tables.GetValue() != 'Ninguna':
			database = self.cbo_databases.GetValue()
			table = self.cbo_tables.GetValue()
			self.tabs.AddPage(View_resgisters(self.tabs,database,table), table.capitalize())
	#self.tabs.AddPage(ver_data(self.tabs), 'Data')
	def tab_generate_data(self,evt):
		items = self.spin_number_items.GetValue()
		gen = Generator()
		if len(self.array_data_preview_generate) != 0:
			n = len(self.array_data_preview_generate)
			r = gen.create_mysql(self.array_data_preview_generate,items,self.cbo_tables.GetValue())
			
			self.tabs.AddPage(ver_data(self.tabs,r), 'Data')

	def insert_into(self,evt):
		items = self.spin_number_items.GetValue()
		gen = Generator()
		registers = ''
		if len(self.array_data_preview_generate) != 0:
			n = len(self.array_data_preview_generate)
			registers = gen.create_mysql(self.array_data_preview_generate,items,self.cbo_tables.GetValue())
			registers = registers.replace(',"");',');')
			registers = registers.replace(',,',',')
			
			self.guardando(registers)

	def guardando(self,content):
		gen = Generator()
		db = gen.connection_server()
		db.DB_NAME = self.cbo_databases.GetValue()

		array = content.split('\n')
		array.pop()

		t = 0

		try:
			for i in array:
				val = db.run_query(str(i).replace(',")','').replace(',"");',');').replace(',,',','))
				if val == None:
					t = t + 1
			
			if t != 0:
				wx.MessageBox("Guardado Complete","Complete",wx.OK | wx.ICON_INFORMATION)
			else:
				wx.MessageBox("Ha ocurrido un error","Error",wx.OK | wx.ICON_INFORMATION)

		except Exception as e:
			wx.MessageBox(str(e),"Error",wx.OK | wx.ICON_INFORMATION)