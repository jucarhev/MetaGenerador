import wx
import wx.xrc
import wx.aui

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
		bSizer17.Add( self.txt_export, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )


		content = content.replace(',"");',');')
		content = content.replace(',,',',')
		self.txt_export.SetValue(content)

	

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

###########################################################################
## Class about
###########################################################################
class about ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 450,439 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MetaGenerador", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
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
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"MetaGenerator", u"https://github.com/pacpac1992/MetaGenerador", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer17.Add( self.m_hyperlink1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Iconos de flaticons: www.flaticon.com \n Madebyoliver, Kirill Kazachek, Freepik \nLicence: Creative Commons BY 3.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer17.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )