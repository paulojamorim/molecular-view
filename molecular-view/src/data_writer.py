#----------------------------------------------------------------------------
# Name:         data_writer.py (module of Molecular View software)
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

class vrml_writer():

    def __init__(self):
        self.filename = ""
        self.renwin = 0

    def set_filename(self, filename):
        self.filename = filename
        
    def set_render(self, render):
        renwin = vtkRenderWindow()
        renwin.SetInput(render)
        self.renwin = renwin
        
    def set_render_window(self, renwin):
        self.renwin = renwin
        
    def write(self):
        from vtk import vtkVRMLExporter, vtkRenderWindow
        
        vrml = vtkVRMLExporter()
        vrml.SetInput(self.renwin)
        vrml.SetFileName(self.filename)
        vrml.Write()
        
class stl_writer():
    
    def __init__(self):
        self.filename = ""
        self.polydata_list = []
        
    def set_filename(self, filename):
        self.filename = filename
        
    def set_input(self, polydata_list):
        self.polydata_list = polydata_list
        
    def write(self):
        from vtk import vtkAppendPolyData, vtkTriangleFilter, vtkSTLWriter
        
        # tie together parts of molecules
        append = vtkAppendPolyData()
        for polydata in self.polydata_list:
            triangles = vtkTriangleFilter()
            triangles.SetInput(polydata)
            append.AddInput(triangles.GetOutput())
            
        # generate stl
        stl_bin = vtkSTLWriter()
        stl_bin.SetInput(append.GetOutput())
        stl_bin.SetFileName(self.filename)
        stl_bin.SetFileType(2) # sets binary and not ascii mode
        stl_bin.Write()
        
        