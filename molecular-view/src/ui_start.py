#!/usr/bin/env python
#Boa:App:BoaApp
#----------------------------------------------------------------------------
# Name:         ui_start.py (module of Molecular View software)
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

import ui_frm_main

modules ={u'ui_frm_main': [1, 'Main frame of Application', u'ui_frm_main.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = ui_frm_main.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
