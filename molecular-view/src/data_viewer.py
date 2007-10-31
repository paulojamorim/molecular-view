#----------------------------------------------------------------------------
# Name:         data_viewer.py (module of Molecular View software)
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

class pdb_viewer():
    
    def __init__(self, prnt):
        from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
        iren = wxVTKRenderWindowInteractor(prnt,-1,size = prnt.GetSize())
        iren.SetPosition((0,0))
        iren.Show(1)
        iren.Render()
        self.iren = iren
        self.prnt = prnt
        
    def set_actor_list(self, actor_list=[]):
        from vtk import vtkRenderer
        
        iren = self.iren
        ren = vtkRenderer()
        ren.SetBackground(0, 0, 0)
        for actor in actor_list:
            ren.AddActor(actor)
        iren.GetRenderWindow().AddRenderer(ren)
        iren.Render()
        
        self.actor_list = actor_list
        self.ren = ren
        
    def set_size(self, new_size):
        iren = self.iren
        iren.SetSize(new_size)
        iren.Render()
        
    def get_render_window(self):
        return self.iren.GetRenderWindow()
    
    def clear(self):
        from vtk import vtkRenderer
        
        iren = self.iren
        ren = self.ren
        actor_list = self.actor_list
        
        iren.GetRenderWindow().RemoveRenderer(ren)
        for actor in actor_list:
            ren.RemoveActor(actor)
        
        ren = vtkRenderer()
        ren.SetBackground(0, 0, 0)
        
        iren.GetRenderWindow().AddRenderer(ren)
        iren.Render()
        
    def exit(self):
        del self.actor_list
        del self.iren
        del self.ren
        
    def hide(self):
        self.iren.Hide()
        
    def show(self, value=1):
        self.iren.Show(value)
        
    def update(self):
        self.iren.Render()
