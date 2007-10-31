#----------------------------------------------------------------------------
# Name:         ui_dlg.py (module of Molecular View software)
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
import os
import sys

def open_file(prnt):
        wildcard = "ENT(*.ent)|*.ent|" \
                   "Protein Data Base (*.pdb)|*.pdb|" \
                   "All files (*.*)|*.*"
                   
        dlg = wx.FileDialog(prnt, message="Choose a file",
                            defaultDir=os.getcwd(), defaultFile="",\
                            wildcard=wildcard, style=wx.OPEN | wx.CHANGE_DIR)
                            
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPaths()[0]
            return path
        
        return 0

def open_another_file(prnt):
        
    dlg = wx.MessageDialog(prnt, "In order to open a new file you should close"+
                                 " the previous one.\n Close the open file?",
                                 "Molecular View", wx.YES_NO|wx.ICON_INFORMATION)
    answer = dlg.ShowModal()
    if answer == wx.ID_YES:
        return 1
    elif answer == wx.ID_NO:
        return 0
        
def about(prnt):
    from wx.lib.wordwrap import wordwrap
    
    info = wx.AboutDialogInfo()
    info.Name = "Molecular View"
    info.Version = "0.0.1 beta"
    info.Copyright = "(C) 2007 Tatiana Al-Chueyr Pereira Martins"
    info.Description = wordwrap(
        "Molecular View program is a software program that shows 3D models "
        "related to PDB (Protein Data Base) files on the display device. "
        
        "\n\nThe software also allows generating the correspondent VRML or STL "
        "files, so the user can build up Molecular Rapid Prototyping physical "
        "models.",
        350, wx.ClientDC(prnt))
    info.WebSite = ("http://www.softwarepublico.gov.br", "InVesalius Community")
    info.Developers = [ "Tatiana Al-Chueyr Pereira Martins",
                        "\nPaulo Henrique Junqueira Amorim",
                        "\nFelipe Faria de Souza" ]

    info.License = "GPL (General Public License) version 2"

    # Then we call wx.AboutBox giving its info object
    wx.AboutBox(info)
    
def save_file(prnt, default_filename=""):
    
    wildcard = "STL(*.stl)|*.stl|"\
               "VRML 2.0 (*.vrml)|*.vrml"
    
    dlg = wx.FileDialog(prnt, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile=default_filename, wildcard=wildcard, style=wx.SAVE)
    
    if dlg.ShowModal() == wx.ID_OK:
        if sys.platform == 'win32':
            filedir = dlg.GetDirectory()+'\\'
        else:
            filedir = dlg.GetDirectory()+'/'
                
        filename = filedir+dlg.GetFilename()
        type = dlg.GetFilterIndex()
        
        if (type == 0):
            filetype = "stl"
        elif (type == 1):
            filetype = "vrml"
            
        return filename, filetype
    
    return []

def unable_to_export(prnt):
    
    dlg = wx.MessageDialog(prnt, "In order to export a file you need to have"+
                                 " opened it previously.",
                                 "Molecular View", wx.OK)
    dlg.ShowModal()
