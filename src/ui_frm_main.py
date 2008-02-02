#Boa:Frame:frm
#----------------------------------------------------------------------------
# Name:         ui_frm_main.py (module of Molecular View software)
# Purpose:      Molecular View is a software for the visualization of PDB 
#               files and can be used for the generation of correspondent 
#               VRML or STL files, for Rapid Prototyping purposes.
#
# Authors:      Tatiana Al-Chueyr Pereira Martins,
#               Paulo Henrique Junqueira Amorim,
#               Felipe Faria de Souza
#
# Created:      October 2007
# Copyright:    (c) 2007 by Tatiana Al-Chueyr Pereira Martins
# Licence:      General Public License 2 (GPL2)
#----------------------------------------------------------------------------

import os
import wx
import wx.gizmos

def create(parent):
    return frm(parent)

[wxID_FRM, wxID_FRMPANEL, 
] = [wx.NewId() for _init_ctrls in range(2)]

[wxID_FRMMENU_HELPITEM_ABOUT, wxID_FRMMENU_HELPITEM_LICENSE, 
] = [wx.NewId() for _init_coll_menu_help_Items in range(2)]

[wxID_FRMMENU_FILEITEMS_EXPORTFILE, wxID_FRMMENU_FILEITEM_CLOSEFILE, 
 wxID_FRMMENU_FILEITEM_EXIT, wxID_FRMMENU_FILEITEM_OPENFILE, 
] = [wx.NewId() for _init_coll_menu_file_Items in range(4)]

[wxID_FRMMENU_VIEWITEM_FULLSCREEN,wxID_FRMMENU_VIEWITEM_STEREOMODE,
] = [wx.NewId() for _init_coll_menu_view_file_Items in range(2)]

[wxID_FRMSUBMENU_VIEWITEM_STEREOOFF,wxID_FRMSUBMENU_VIEWITEM_STEREOCRYSTALEYES,
wxID_FRMSUBMENU_VIEWITEM_STEREOINTERLACED, wxID_FRMSUBMENU_VIEWITEM_STEREOREDBLUE,
wxID_FRMSUBMENU_VIEWITEM_STEREOLEFT, wxID_FRMSUBMENU_VIEWITEM_STEREORIGHT,
wxID_FRMSUBMENU_VIEWITEM_STEREODRESDEN,
] = [wx.NewId() for _init_coll_submenu_view_stereo_Items in range(7)]


class frm(wx.Frame):
    def _init_sizers(self):
        # generated method, don't edit
        self.boxsizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_boxsizer_Items(self.boxsizer)

        self.SetSizer(self.boxsizer)


    def _init_coll_boxsizer_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.panel, 1, border=0, flag=wx.GROW | wx.EXPAND)

    def _init_coll_menubar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu_file, title='File')
        parent.Append(menu=self.menu_view, title='View')
        parent.Append(menu=self.menu_help, title='Help')

    def _init_utils(self):
        # generated method, don't edit
        self.menubar = wx.MenuBar()
        self.menubar.SetAutoLayout(True)

        self.menu_file = wx.Menu(title='')
        self.menu_view = wx.Menu(title='')
        self.submenu_stereo = wx.Menu(title='')
        self.menu_help = wx.Menu(title='')

        self._init_coll_menubar_Menus(self.menubar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRM, name='frm', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1000, 700),
              style=wx.DEFAULT_FRAME_STYLE, title='Molecular View')
        self._init_utils()
        self.SetMenuBar(self.menubar)
        self.SetIcon(wx.Icon(os.path.abspath('../img/molecule.ico'),
              wx.BITMAP_TYPE_ICO))

        self.panel = wx.Panel(id=wxID_FRMPANEL, name='panel', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(992, 666),
              style=wx.TAB_TRAVERSAL)
        self.panel.SetBackgroundColour(wx.Colour(128, 128, 128))

        self._init_sizers()

    def __init__(self, parent):
        from controller import controller
        
        self.controller = controller(self)
        
        self._init_ctrls(parent)        
        self._init_menu_file(self.menu_file)
        self._init_submenu_view_stereo(self.submenu_stereo)
        self._init_menu_view(self.menu_view)
        self._init_menu_help(self.menu_help)
        self.init_evt()
        #self.Maximize()

    def _init_menu_file(self, parent):

        item = wx.MenuItem(parent, wxID_FRMMENU_FILEITEM_OPENFILE,
                            'Open...', 'Open PDB file')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/openfile.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
        
        item = wx.MenuItem(parent, wxID_FRMMENU_FILEITEMS_EXPORTFILE,
                           'Export...', 'Export file')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/exportfile.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
        
        item = wx.MenuItem(parent, wxID_FRMMENU_FILEITEM_CLOSEFILE,
                            'Close', 'Close file')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/closefile.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
        
        item = wx.MenuItem(parent, wxID_FRMMENU_FILEITEM_EXIT,
                            'Exit Molecular View', 'Exit Molecular View')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/exit.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)

    def _init_menu_help(self, parent):

        item = wx.MenuItem(parent, wxID_FRMMENU_HELPITEM_LICENSE,
                            'License', 'Software license')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/gpl.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
            
        item = wx.MenuItem(parent, wxID_FRMMENU_HELPITEM_ABOUT,
                            'About Molecular View', 'About Molecular View')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/molecule.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
        
    def _init_menu_view(self, parent):
        
        item = wx.MenuItem(parent, wxID_FRMMENU_VIEWITEM_FULLSCREEN,
                           'Fullscreen\tCtrl+F', 'Show main panel in fullscreen mode')
        parent.AppendItem(item)
        parent.AppendSeparator()
        
        parent.AppendMenu(help='Stereo mode', id=wxID_FRMMENU_VIEWITEM_STEREOMODE,
                            submenu=self.submenu_stereo, text='Stereo mode')
    
    def _init_submenu_view_stereo(self, parent):
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREOOFF,
              kind=wx.ITEM_RADIO, text='Off')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREOCRYSTALEYES,
              kind=wx.ITEM_RADIO, text='CrystalEyes')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREOINTERLACED,
              kind=wx.ITEM_RADIO, text='Interlaced')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREOREDBLUE,
              kind=wx.ITEM_RADIO, text='RedBlue')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREOLEFT,
              kind=wx.ITEM_RADIO, text='Left')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREORIGHT,
              kind=wx.ITEM_RADIO, text='Right')
        parent.Append(help='', id=wxID_FRMSUBMENU_VIEWITEM_STEREODRESDEN,
              kind=wx.ITEM_RADIO, text='Dresden')
        
        
        
    def init_evt(self):
        self.Bind(wx.EVT_SIZE, self.resize)
           
        self.Bind(wx.EVT_MENU, self.open_file,
              id=wxID_FRMMENU_FILEITEM_OPENFILE)

        self.Bind(wx.EVT_MENU, self.exit, id=wxID_FRMMENU_FILEITEM_EXIT)
        
        self.Bind(wx.EVT_MENU, self.close_file,
              id=wxID_FRMMENU_FILEITEM_CLOSEFILE)
        
        self.Bind(wx.EVT_MENU, self.export_file,
              id=wxID_FRMMENU_FILEITEMS_EXPORTFILE)
              
        self.Bind(wx.EVT_MENU, self.show_about, id=wxID_FRMMENU_HELPITEM_ABOUT)
        self.Bind(wx.EVT_MENU, self.show_license, id=wxID_FRMMENU_HELPITEM_LICENSE)
        
        self.Bind(wx.EVT_MENU, self.fullscreen, id=wxID_FRMMENU_VIEWITEM_FULLSCREEN)
        
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 0),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREOOFF)
                    
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'CrystalEyes'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREOCRYSTALEYES)
        
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'RedBlue'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREOREDBLUE)
                    
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'Interlaced'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREOINTERLACED)
                    
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'Left'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREOLEFT)

        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'Right'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREORIGHT)
                    
        self.Bind(wx.EVT_MENU, lambda e, s = self:self.set_stereo_mode(e, 1, 'Dresden'),
                    id=wxID_FRMSUBMENU_VIEWITEM_STEREODRESDEN)
                    
        
                    
        
    def resize(self, event):
        self.Layout()
        self.controller.resize_ui(self.panel.GetSize())
        event.Skip()
    
    def get_data_panel(self):
        return self.panel
    
    def open_file(self, event):
        self.controller.open_file()
        event.Skip()

    def show_about(self, event):
        self.controller.show_about_dlg()
        event.Skip()

    def set_header(self, filename=""):
        if filename:
            self.SetTitle(filename+' - Molecular View')
        else:
            self.SetTitle('Molecular View')

    def exit(self, event):
        self.controller.exit()
        self.Close()
        event.Skip()

    def close_file(self, event):
        self.controller.close_file()
        event.Skip()

    def export_file(self, event):
        self.controller.export_file()
        event.Skip()

    def show_license(self, event):
        self.controller.show_license()
        event.Skip()
    
    def set_stereo_mode(self, event, on=True, mode='RedBlue'):
        self.controller.set_stereo_mode(on, mode)
        event.Skip()
        
    def fullscreen(self, event=None, on=1):
        self.ShowFullScreen(on)
        self.controller.set_viewer_fullscreen()
        if event:
            event.Skip()