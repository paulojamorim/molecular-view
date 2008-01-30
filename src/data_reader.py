#----------------------------------------------------------------------------
# Name:         data_reader.py (module of Molecular View software)
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

class pdb_reader():

    def __init__(self):
        self.data = 0
        self.filename = ""
        self.molecule_on = 1
        self.tubes_on = 1
        self.actor_list = []
        self.polydata_list = []

    def set_filename(self, filename):
        self.filename = filename

    def read(self):
        from vtk import vtkPDBReader, vtkSphereSource, vtkGlyph3D, \
                        vtkPolyDataMapper, vtkLODActor, vtkTubeFilter
        
        actor_list = self.actor_list
        polydata_list = self.polydata_list
        
        pdb = vtkPDBReader()
        pdb.SetFileName(self.filename)
        pdb.SetHBScale(1.0)
        pdb.SetBScale(1.0)
        
        if self.molecule_on:
            sphere = vtkSphereSource()
            sphere.SetCenter(0, 0, 0)
            sphere.SetRadius(1)
            sphere.SetThetaResolution(8)
            sphere.SetStartTheta(0)
            sphere.SetEndTheta(360)
            sphere.SetPhiResolution(8)
            sphere.SetStartPhi(0)
            sphere.SetEndPhi(180)
            
            glyph = vtkGlyph3D()
            glyph.SetInputConnection(pdb.GetOutputPort())
            #glyph.SetOrient(1)
            glyph.SetColorMode(1)
            glyph.ScalingOn()
            glyph.SetScaleMode(2)
            glyph.SetScaleFactor(0.25)
            glyph.SetSource(sphere.GetOutput())
            
            mapper = vtkPolyDataMapper()
            mapper.SetInputConnection(glyph.GetOutputPort())
            mapper.SetImmediateModeRendering(1)
            mapper.UseLookupTableScalarRangeOff()
            mapper.SetScalarVisibility(1)
            mapper.SetScalarModeToDefault()
            
            actor = vtkLODActor()
            actor.SetMapper(mapper)
            #actor.GetProperty().SetRepresentationToSurface()
            #actor.GetProperty().SetInterpolationToGouraud()
            #actor.GetProperty().SetAmbient(0.15)
            #actor.GetProperty().SetDiffuse(0.85)
            #actor.GetProperty().SetSpecular(0.1)
            #actor.GetProperty().SetSpecularPower(100)
            #actor.GetProperty().SetSpecularColor(1, 1, 1)
            #actor.GetProperty().SetColor(1, 1, 1)
            actor.SetNumberOfCloudPoints(30000)
            
            actor_list.append(actor)
            polydata_list.append(glyph.GetOutput())
        
        if self.tubes_on:
            tubes = vtkTubeFilter()
            tubes.SetInputConnection(pdb.GetOutputPort())
            tubes.SetNumberOfSides(8)
            tubes.SetCapping(0)
            tubes.SetRadius(0.2)
            tubes.SetVaryRadius(0)
            tubes.SetRadiusFactor(10)
    
            tube_mapper = vtkPolyDataMapper()
            tube_mapper.SetInputConnection(tubes.GetOutputPort())
            tube_mapper.SetImmediateModeRendering(1)
            tube_mapper.UseLookupTableScalarRangeOff()
            tube_mapper.SetScalarVisibility(1)
            tube_mapper.SetScalarModeToDefault()
    
            tube_actor = vtkLODActor()
            tube_actor.SetMapper(tube_mapper)
            #tub_actor.GetProperty().SetRepresentationToSurface()
            #tub_actor.GetProperty().SetInterpolationToGouraud()
            #tub_actor.GetProperty().SetAmbient(0.15)
            #tub_actor.GetProperty().SetDiffuse(0.85)
            #tub_actor.GetProperty().SetSpecular(0.1)
            #tub_actor.GetProperty().SetSpecularPower(100)
            #tub_actor.GetProperty().SetSpecularColor(1, 1, 1)
            #tub_actor.GetProperty().SetColor(1, 1, 1)
            tube_actor.SetNumberOfCloudPoints(30000)
            
            actor_list.append(tube_actor)
            polydata_list.append(tubes.GetOutput())
        
        return actor_list, polydata_list

    def show_tubes(self, show=1):
        self.tubes_on = show
        
    def show_molecules(self, show=1):
        self.molecules_on = show