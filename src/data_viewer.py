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
    
    def __init__(self, prnt, controller=None):
        from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
        from vtk import vtkRenderWindow, vtkRenderer, vtkInteractorStyleRubberBandPick
        import wx
        
        self.prnt = prnt
        self.fullscreen_on = 0

        iren = wxVTKRenderWindowInteractor(self.prnt,-1,size = self.prnt.GetSize(), stereo=1)
        #iren.AddObserver("KeyPressEvent", self.key_down)
        iren.AddObserver("CharEvent", self.key_down)
        iren.SetPosition((0,0))
        iren.SetDesiredUpdateRate(1)
        style = vtkInteractorStyleRubberBandPick() 
        iren.SetInteractorStyle(style)

        iren.Enable(1)        
        self.iren = iren
        
        self.controller = controller
        
    def key_down(self, event, event_name):

        if ((event.GetKeyCode() == 'f') or (event.GetKeyCode() == 'F')):
            if self.fullscreen_on:
                self.fullscreen(False)
            
            else:
                self.fullscreen(True)
            self.controller.set_frame_fullscreen(self.fullscreen_on)
            
    def fullscreen(self, on=True):
        self.fullscreen_on = on
        
        
    def set_stereo_mode(self, on=True, mode="CrystalEyes"):
        """set_stereo_mode(on = [_True_, False], type = [_"CrystalEyes"_, 
        "RedBlue", "Interlaced", "Left", "Right", "Dresden"]
        """
        iren = self.iren
        renwin = iren.GetRenderWindow()
        if on:
            renwin.StereoRenderOn()
            exec("renwin.SetStereoTypeTo"+mode+"()")
        else:
            renwin.StereoRenderOff()
            
        iren.Render()
        
    def set_actor_list(self, actor_list=[]):
        from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
        from vtk import vtkRenderWindow, vtkRenderer

        iren = self.iren
        
        ren = vtkRenderer()
        ren.SetBackground(0, 0, 0)
        for actor in actor_list:
            ren.AddActor(actor)
            
        iren.GetRenderWindow().AddRenderer(ren)
        iren.Render()
        
        self.actor_list = actor_list
        self.ren = ren
        self.iren = iren
        
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
