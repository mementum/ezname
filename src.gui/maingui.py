# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Patterns" ), wx.HORIZONTAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.HORIZONTAL )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"File Extensions", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlKnownExtensions = wx.TextCtrl( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_textCtrlKnownExtensions, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Use \";\" to separate the extensions.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gbSizer1.AddGrowableCol( 1 )
		
		sbSizer71.Add( gbSizer1, 0, 0, 5 )
		
		self.m_staticline4 = wx.StaticLine( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer71.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"RegExp Files/Dirs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlRExp = wx.TextCtrl( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrlRExp, 1, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"RegExp Directorize", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRegExpDirectorize = wx.TextCtrl( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrlRegExpDirectorize, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		sbSizer71.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( sbSizer71, 0, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Work Directory" ), wx.HORIZONTAL )
		
		self.m_dirPickerWorkDir = wx.DirPickerCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
		sbSizer5.Add( self.m_dirPickerWorkDir, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer23.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Target Directorize Dir" ), wx.VERTICAL )
		
		self.m_dirPickerDirDirectorize = wx.DirPickerCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer9.Add( self.m_dirPickerDirDirectorize, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer23.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Parameters" ), wx.VERTICAL )
		
		self.m_checkBoxLoadOnStart = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Load Files on Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBoxLoadOnStart, 0, wx.ALL, 5 )
		
		self.m_checkBoxDirsDelete = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Delete Subdirectories", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBoxDirsDelete, 0, wx.ALL, 5 )
		
		self.m_checkBoxDirsPurgeEmpty = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Purge Empty Subdirectories", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBoxDirsPurgeEmpty, 0, wx.ALL, 5 )
		
		self.m_checkBoxMoveDirectorize = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Move to Directorize", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBoxMoveDirectorize, 0, wx.ALL, 5 )
		
		self.m_checkBoxRunDry = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Dry Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBoxRunDry, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Original Filenames" ), wx.VERTICAL )
		
		m_listBoxFnOriginalChoices = []
		self.m_listBoxFnOriginal = wx.ListBox( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxFnOriginalChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		self.m_listBoxFnOriginal.SetMinSize( wx.Size( 400,400 ) )
		
		sbSizer6.Add( self.m_listBoxFnOriginal, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Final Filenames" ), wx.VERTICAL )
		
		m_listBoxFnFinalChoices = []
		self.m_listBoxFnFinal = wx.ListBox( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxFnFinalChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		self.m_listBoxFnFinal.SetMinSize( wx.Size( 400,-1 ) )
		
		sbSizer7.Add( self.m_listBoxFnFinal, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer22.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer22.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonRefresh = wx.Button( self.m_panel1, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_buttonRefresh, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Consolas" ) )
		
		bSizer22.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonExecute = wx.Button( self.m_panel1, wx.ID_ANY, u"Execute", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_buttonExecute, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Consolas" ) )
		
		bSizer22.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonRefreshDirectorize = wx.Button( self.m_panel1, wx.ID_ANY, u"Direct. Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_buttonRefreshDirectorize, 0, wx.ALL, 5 )
		
		self.m_staticText711 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )
		self.m_staticText711.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Consolas" ) )
		
		bSizer22.Add( self.m_staticText711, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonExecuteDirectorize = wx.Button( self.m_panel1, wx.ID_ANY, u"Directorize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_buttonExecuteDirectorize, 0, wx.ALL, 5 )
		
		
		bSizer22.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonOpenLog = wx.Button( self.m_panel1, wx.ID_ANY, u"Open Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_buttonOpenLog, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_panelLog = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelLog.Hide()
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.m_panelLog, wx.ID_ANY, u"Execution Log" ), wx.VERTICAL )
		
		self.m_textCtrlLogExecution = wx.TextCtrl( sbSizer61.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), wx.HSCROLL|wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer61.Add( self.m_textCtrlLogExecution, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		
		self.m_panelLog.SetSizer( bSizer8 )
		self.m_panelLog.Layout()
		bSizer8.Fit( self.m_panelLog )
		bSizer13.Add( self.m_panelLog, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer14 )
		self.m_panel1.Layout()
		bSizer14.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemClearRegistry = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Clear Registry", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemClearRegistry )
		
		self.m_menuItemAboutDialog = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"&About ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemAboutDialog )
		
		self.m_menubar1.Append( self.m_menu1, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolAboutDialog = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"About ...", wx.ArtProvider.GetBitmap( u"priv/icons/information.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"About ...", u"Show the About Dialog", None ) 
		
		self.m_toolBar1.Realize() 
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookAbout = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panelAbout = wx.Panel( self.m_notebookAbout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextAppNameVersion = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextAppNameVersion.Wrap( -1 )
		bSizer10.Add( self.m_staticTextAppNameVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextCopyright = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextCopyright.Wrap( -1 )
		bSizer10.Add( self.m_staticTextCopyright, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlinkURL = wx.HyperlinkCtrl( self.m_panelAbout, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
		bSizer10.Add( self.m_hyperlinkURL, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panelAbout.SetSizer( bSizer10 )
		self.m_panelAbout.Layout()
		bSizer10.Fit( self.m_panelAbout )
		self.m_notebookAbout.AddPage( self.m_panelAbout, u"About", True )
		
		bSizer8.Add( self.m_notebookAbout, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_buttonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelAboutDocument
###########################################################################

class PanelAboutDocument ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlDocument = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer111.Add( self.m_textCtrlDocument, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer111 )
		self.Layout()
		bSizer111.Fit( self )
	
	def __del__( self ):
		pass
	

