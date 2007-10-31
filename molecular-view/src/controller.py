#----------------------------------------------------------------------------
# Name:         controller.py (module of Molecular View software)
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

import sys

class controller():
    
    def __init__(self, frame):
        self.ui_frame = frame
        self.load = 0
        self.file_open = 0
        self.polydata_list = []
        self.filename = ""
        
    def open_file(self):
        from data_reader import pdb_reader
        from data_viewer import pdb_viewer
        import ui_dlg
        
        prnt_frm = self.ui_frame
        file_open = self.file_open
        load = self.load

        if not load:
            viewer = pdb_viewer(prnt_frm.get_data_panel())
            self.data_viewer = viewer
        
        viewer = self.data_viewer
        
        if file_open:
            if ui_dlg.open_another_file(prnt_frm):
                viewer.clear()
                prnt_frm.set_header()
                file_open = 0
            else:
                viewer.update()

        if (not load) or (not file_open):
            path = ui_dlg.open_file(prnt_frm)
            if path:
                if sys.platform == 'win32':
                    name = path.split('\\')[-1]
                else:
                    name = path.split('/')[-1]
                prnt_frm.set_header(filename=name)
                self.filename = name.split('.')[0]
                
                reader = pdb_reader()
                reader.set_filename(path)
                
                (actor_list, self.polydata_list)  = reader.read()
                
                viewer.set_actor_list(actor_list)
                viewer.show()
                load = 1
                file_open = 1
                
        self.file_open = file_open
        self.load = load
        

    def export_file(self):
        import ui_dlg
        from data_writer import vrml_writer, stl_writer
        
        viewer = self.data_viewer
        frame = self.ui_frame
        
        if not self.file_open:
            # show msg saying there is nothing to be exported
            ui_dlg.unable_to_export(frame)
        else:
            answer = ui_dlg.save_file(frame, self.filename)
            if answer:
                filename = answer[0]
                filetype = answer[1]
                
                if filetype == "vrml":
                    writer = vrml_writer()
                    writer.set_render_window(viewer.get_render_window())
                elif filetype == "stl":
                    writer = stl_writer()
                    writer.set_input(self.polydata_list)
                    
                writer.set_filename(filename)
                writer.write()
                
    def resize_ui(self, new_size):
        try:
            getattr(self, "data_viewer")
        except AttributeError:
            print "Attribute Error - data_viewer"
            pass
        else:
            self.data_viewer.set_size(new_size)

    def show_about_dlg(self):
        import ui_dlg
        ui_dlg.about(self.ui_frame)
        
    def exit(self):
        try:
            getattr(self, "data_viewer")
        except AttributeError:
            print "Attribute Error - data_viewer"
            pass
        else:
            self.data_viewer.exit()
            del self.data_viewer
        del self.load
        del self.file_open
        del self.ui_frame
        
    def close_file(self):
        self.file_open = 0
        self.data_viewer.clear()
        self.data_viewer.hide()
        self.ui_frame.set_header()
        
    def show_license(self):
        from ui_frm_license import mini_frm
        
        license_frm = mini_frm(self.ui_frame)
        license_frm.Show()
        
        
