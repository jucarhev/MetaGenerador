# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## Update by juankarlos.0304@gmail.com
###########################################################################

import wx
import wx.xrc

# Import class
from Generator import *

###########################################################################
## Class GUI
###########################################################################

class GUI ( wx.Frame ):
	
	array_data_preview_generate = []

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generador", pos = wx.DefaultPosition, size = wx.Size( 512,422 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		favicon = wx.Icon('src/icon/notebook.png',wx.BITMAP_TYPE_PNG, 16,16)
		self.SetIcon(favicon)
		self.gui()
		self.SetSize((600,530))
		self.SetTitle("Generate Data")
		self.Centre()
		self.Show()

		self.check_start()
		self.start_file_list()
		
	def gui(self):
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.file_menu_export = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.file_menu_export )
		
		self.file_menu_newlist = wx.MenuItem( self.file_menu, wx.ID_ANY, u"New list", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.file_menu_newlist )
		
		self.file_menu_close = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.file_menu_close )
		
		self.menubar.Append( self.file_menu, u"&File" ) 
		
		self.edit_menu = wx.Menu()
		self.edit_menu_preferences = wx.MenuItem( self.edit_menu, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.edit_menu_preferences )
		
		self.edit_menu_database = wx.MenuItem( self.edit_menu, wx.ID_ANY, u"Databas conenction", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.edit_menu_database )
		
		self.edit_menu_list = wx.MenuItem( self.edit_menu, wx.ID_ANY, u"list", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.edit_menu_list )
		
		self.menubar.Append( self.edit_menu, u"&Edit" ) 
		
		self.help_menu = wx.Menu()
		self.help_menu_about = wx.MenuItem( self.help_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.help_menu_about )
		
		self.menubar.Append( self.help_menu, u"Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.tool_new_document = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icon/new-file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
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
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
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
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
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
		
		self.txt_config = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.txt_config, 0, wx.ALL, 5 )
		
		self.btn_help_list = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"src/icon/info16x16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer6.Add( self.btn_help_list, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.spin_number_items = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 500, 1 )
		bSizer7.Add( self.spin_number_items, 0, wx.ALL, 5 )
		
		self.btn_play = wx.Button( self, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btn_play, 0, wx.ALL, 5 )
		
		self.btn_clean = wx.Button( self, wx.ID_ANY, u"Clean", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btn_clean, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.list_preview = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.list_preview.InsertColumn(0, 'Num', width=50)
		self.list_preview.InsertColumn(1, 'Column', width=100)
		self.list_preview.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 80)
		self.list_preview.InsertColumn(3, 'Content', wx.LIST_FORMAT_RIGHT, 90)
		self.list_preview.InsertColumn(4, 'Example', wx.LIST_FORMAT_RIGHT, 220)
		bSizer8.Add( self.list_preview, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		#Menu
		self.Bind(wx.EVT_MENU, self.menu_file_close, self.file_menu_close)
		self.Bind(wx.EVT_MENU, self.menu_file_export, self.file_menu_export)
		self.Bind(wx.EVT_MENU, self.menu_file_newlist, self.file_menu_newlist)
		self.Bind(wx.EVT_MENU, self.menu_edit_preferences ,self.edit_menu_preferences)
		self.Bind(wx.EVT_MENU, self.menu_edit_databases ,self.edit_menu_database)
		self.Bind(wx.EVT_MENU, self.menu_edit_menulist ,self.edit_menu_list)
		self.Bind(wx.EVT_MENU, self.OnAboutBox, self.help_menu_about)

		#ToolBar
		self.Bind(wx.EVT_TOOL, self.menu_file_newlist, self.tool_new_document)
		self.Bind(wx.EVT_TOOL, self.menu_edit_databases, self.tool_database)
		self.Bind(wx.EVT_TOOL, self.menu_file_export, self.tool_export)
		self.Bind(wx.EVT_TOOL, self.menu_edit_preferences, self.tool_preferences)
		self.Bind(wx.EVT_TOOL, self.OnAboutBox, self.tool_help)
		self.Bind(wx.EVT_TOOL, self.menu_file_close, self.tool_close)

		#Botones
		self.btn_play.Bind(wx.EVT_BUTTON,self.preview_info)
		self.btn_clean.Bind(wx.EVT_BUTTON,self.clean_info)
		self.btn_describe_table.Bind(wx.EVT_BUTTON,self.describe_table_database)
		self.btn_help_list.Bind(wx.EVT_BUTTON,self.help_list_description)

		#Combos
		self.cbo_databases.Bind(wx.EVT_COMBOBOX, self.combo_change_databases)
		self.cbo_tables.Bind(wx.EVT_COMBOBOX, self.combo_change_tables)

		self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onListBox, self.list_preview)
	
	#####################################
	#			Methods Menu 			
	#####################################
	def menu_file_close(self, event):
		self.Destroy()

	def menu_file_export(self,event):
		items = self.spin_number_items.GetValue()
		gen = Generator()
		if len(self.array_data_preview_generate) != 0:
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
		pass

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
				content = '\nParams: 8,md5 / 8,sha1 / 8'
				wx.MessageBox('Return password, Example: '+content,'Password', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Random':
				content = '\nParams None / 0,200(star-end)'
				wx.MessageBox('Return Random, Example: '+content,'Random', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Feature':
				content = '\nParams None / uno,dos,tres'
				wx.MessageBox('Return Feature value of the array, Example: '+content,'Feature', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Telephone':
				content = '\nParams None / Home(01 ) '
				wx.MessageBox('Return Telephone value of the array, Example: '+content,'Telephone', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Direction':
				content = '\nParams None / Home(01 ) '
				wx.MessageBox('Return Direction value of the array, Example: '+content,'Direction', wx.OK | wx.ICON_INFORMATION)
			elif self.cbo_list.GetValue() == 'Date':
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
		array1 = ['Ninguna','Email','Password','Date','Random','Feature','Telephone','Direction']
		array2 = gen.list_files_diccionary()
		self.cbo_list.AppendItems(array1 + array2)


	#
	def OnAboutBox(self,evt):
		description = "MetaGenerador\n Generador de datos para mysql en formatos\n"
		description = description + "como MySQL\n"
		description = description + "escrito en wxpython , python 3\n"

		licence = "Esta biblioteca es software libre; puede redistribuirla\ny/o modificarla bajo los términos de la\n"
		licence = licence + "Licencia Pública General Reducida de GNU tal como la publica la\n"
		licence = licence + "Free SoftwareFoundation; ya sea la versión 2.1 de la licencia o \n"
		licence = licence + "(según su criterio) cualquier versión posterior."

		info = wx.AboutDialogInfo()

		info.SetIcon(wx.Icon('src/icon/notebook128x128.png', wx.BITMAP_TYPE_PNG))
		info.SetName('MetaGenerador')
		info.SetVersion('0.5')
		info.SetDescription(description)
		info.SetCopyright('(C) 2006 - 2026 juankarlos.0304@gmail.com')
		info.SetWebSite('http://www.pacpac1992.github.io')
		info.SetLicence(licence)
		info.AddDeveloper('JC juankarlos.0304@gmail.com')
		info.AddDocWriter('JC juankarlos.0304@gmail.com')
		info.AddArtist('Iconos de flaticons: www.flaticon.com \n Madebyoliver, Kirill Kazachek, Freepik \nLicence: Creative Commons BY 3.0')
		info.AddTranslator('-----')

		wx.AboutBox(info)

###########################################################################
## Class database_dialog
###########################################################################

class database_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Database connection", pos = wx.DefaultPosition, size = wx.Size( 323,179 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
		file_check = self.gen.file_open('conn.txt','src/config/')
		array_data_connect_server =  file_check.split("\n")
		self.txt_hostname.SetValue(array_data_connect_server[0])
		self.txt_username.SetValue(array_data_connect_server[1])
		self.txt_password.SetValue(array_data_connect_server[2])

		self.btn_save_connection.Bind(wx.EVT_BUTTON,self.save_config)
		self.btn_test_connection.Bind(wx.EVT_BUTTON,self.test_config)
	
	def save_config(self,evt):
		try:
			content = self.txt_hostname.GetValue() + "\n" + self.txt_username.GetValue() + "\n" + self.txt_password.GetValue()
			self.gen.write_file('conn.txt', content ,'src/config/')
			wx.MessageBox("Ok, Change", 'Ok', wx.OK | wx.ICON_INFORMATION)
		except Exception as e:
			wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)
		
	def test_config(self,evt):
		if self.gen.check_connect() == True:
			wx.MessageBox("Ok, Good", 'Ok', wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Fail", 'Error', wx.OK | wx.ICON_ERROR)
	

###########################################################################
## Class setting_dialog
###########################################################################

class setting_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preferences", pos = wx.DefaultPosition, size = wx.Size( 285,189 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
		file_check = self.gen.file_open('preferences.txt','src/config/')
		array_preferences = file_check.split('\n')
		self.txt_exclude_databases.SetValue(array_preferences[0])
		self.txt_exclude_columns.SetValue(array_preferences[1])
		
		self.btn_save_preferences.Bind(wx.EVT_BUTTON,self.save_config)

	def save_config(self,evt):
		try:
			content = self.txt_exclude_databases.GetValue() + '\n' + self.txt_exclude_columns.GetValue()
			self.gen.write_file('preferences.txt', content ,'src/config/')
			wx.MessageBox("Ok, Change", 'Ok', wx.OK | wx.ICON_INFORMATION)
		except Exception as e:
			wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)

###########################################################################
## Class list_dialog
###########################################################################

class list_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lists", pos = wx.DefaultPosition, size = wx.Size( 341,227 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		lst_lista_archivosChoices = []
		self.lst_lista_archivos = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,200 ), lst_lista_archivosChoices, 0 )
		bSizer11.Add( self.lst_lista_archivos, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn_delete_list = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btn_delete_list, 0, wx.ALL, 5 )
		
		self.btn_edit_list = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btn_edit_list, 0, wx.ALL, 5 )
		
		self.btn_save_list = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btn_save_list, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		lst_list_edicionChoices = []
		self.lst_list_edicion = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,200 ), lst_list_edicionChoices, 0 )
		bSizer13.Add( self.lst_list_edicion, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class newdocument_dialog
###########################################################################

class newdocument_dialog ( wx.Dialog ):
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New document", pos = wx.DefaultPosition, size = wx.Size( 237,267 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
	

###########################################################################
## Class export_dialog
###########################################################################

class export_dialog ( wx.Dialog ):
	
	def __init__( self, parent, content ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Export", pos = wx.DefaultPosition, size = wx.Size( 487,332 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt_export = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,300 ), wx.TE_MULTILINE )
		bSizer17.Add( self.txt_export, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.txt_export.SetValue(content)
	
	def __del__( self ):
		pass
	

###########################################################################
## Class description_table
###########################################################################

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

		for ar in rows:
			index = self.list.InsertStringItem(sys.maxint, str(ar[0]))
			self.list.SetStringItem(index, 1, str(ar[1]))
			self.list.SetStringItem(index, 2, str(ar[2]))
			self.list.SetStringItem(index, 3, str(ar[3]))
			self.list.SetStringItem(index, 4, str(ar[4]))
			self.list.SetStringItem(index, 5, str(ar[5]))