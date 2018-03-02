import wx
import wx.xrc
import wx.aui

from Generator import *

"""
Tabs.py
Content:	Panels de los Tabs
Sices: 		v1.0
Clases: 	
"""

class View_resgisters(wx.Panel):
	def __init__(self, parent,db,table):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		database = db
		tb = table
		
		sizer = wx.BoxSizer(wx.VERTICAL)

		id=wx.NewId()
		self.lista=wx.ListCtrl(self,id,style=wx.LC_REPORT|wx.SUNKEN_BORDER,pos=(0,0),size=(555,280))
		sizer.Add(self.lista, 1, wx.EXPAND)
		self.SetSizer(sizer)

		g = Generator()
		conn = g.connection_server(database)
		rows = conn.run_query("SHOW COLUMNS FROM  " + tb)

		c = 0
		for row in rows:
			if c == 0:
				self.primera_columna_db = str(row[0])
			self.lista.InsertColumn(c, row[0])
			c = c+1

		rows = ''
		rows = conn.run_query("SELECT * FROM  "+ tb)
		arreglo = []
		for row in rows:
			arreglo.append(row)

		for ar in arreglo:
			index = self.lista.InsertStringItem(sys.maxint, str(ar[0]))
			for er in range(1,c):
				self.lista.SetStringItem(index, er, str(ar[er]))

class ver_data(wx.Panel):
	"""docstring for ClassName"""
	def __init__(self, parent,content):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		
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