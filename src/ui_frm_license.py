#Boa:MiniFrame:mini_frm
#----------------------------------------------------------------------------
# Name:         ui_frm_license.py (module of Molecular View software)
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

import wx
import wx.html
import os

def create(parent):
    return mini_frm(parent)

[wxID_MINI_FRM, wxID_MINI_FRMHTML_WINDOW, 
] = [wx.NewId() for _init_ctrls in range(2)]

class mini_frm(wx.MiniFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MiniFrame.__init__(self, id=wxID_MINI_FRM, name='mini_frm',
              parent=prnt, pos=wx.Point(382, 165), size=wx.Size(794, 499),
              style=wx.DEFAULT_FRAME_STYLE, title='Molecular View License')
        self.SetClientSize(wx.Size(778, 463))
        self.SetToolTipString('Molecular View - License')
        self.SetIcon(wx.Icon(os.path.abspath('../img/molecule.ico'),
              wx.BITMAP_TYPE_ICO))

        self.html_window = wx.html.HtmlWindow(id=wxID_MINI_FRMHTML_WINDOW,
              name='htmlWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(778, 463), style=wx.html.HW_SCROLLBAR_AUTO)
        self.html_window.SetBackgroundColour(wx.Colour(192, 192, 192))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_html()

    def init_html(self):
        from license import gpl2_license
        self.html_window.SetPage(gpl2_license)
        
        
        
        
        
        
        
        
        
        
