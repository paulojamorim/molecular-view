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

class frm(wx.Frame):
    def _init_coll_menubar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu_file, title='File')
        parent.Append(menu=self.menu_help, title='Help')

    def _init_coll_menu_file_Items(self, parent):
        # generated method, don't edit

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
        


    def _init_coll_menu_help_Items(self, parent):
        # generated method, don't edit


        item = wx.MenuItem(parent, wxID_FRMMENU_HELPITEM_LICENSE,
                            'License', 'Software license')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/gpl.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)
            
        item = wx.MenuItem(parent, wxID_FRMMENU_HELPITEM_ABOUT,
                            'About Molecular View', 'About Molecular View')
        item.SetBitmap(wx.Bitmap(os.path.abspath('../img/molecule.gif'), wx.BITMAP_TYPE_GIF))
        parent.AppendItem(item)

    def _init_utils(self):
        # generated method, don't edit
        self.menubar = wx.MenuBar()
        self.menubar.SetAutoLayout(True)

        self.menu_file = wx.Menu(title='')

        self.menu_help = wx.Menu(title='')

        self._init_coll_menubar_Menus(self.menubar)
        self._init_coll_menu_file_Items(self.menu_file)
        self._init_coll_menu_help_Items(self.menu_help)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRM, name='frm', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1000, 700),
              style=wx.DEFAULT_FRAME_STYLE, title='Molecular View')
        self._init_utils()
        self.SetMenuBar(self.menubar)
        self.SetIcon(wx.Icon(os.path.abspath('../img/molecule.ico'),wx.BITMAP_TYPE_ICO))

        self.panel = wx.Panel(id=wxID_FRMPANEL, name='panel', parent=self,
              pos=wx.Point(23, 0), size=wx.Size(597, 409),
              style=wx.TAB_TRAVERSAL)
        self.panel.SetBackgroundColour(wx.Colour(128, 128, 128))

    def __init__(self, parent):
        from controller import controller
        
        self.controller = controller(self)
        
        self._init_ctrls(parent)        
        self.init_evt()
        #self.Maximize()
        
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
    
