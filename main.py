from tkinter import *
from tkinter import ttk
from colors import *
import os
root = Tk()

names_dict = {'Sebastian Mielczarek':'SM',
                    'Magda':'Mg'       
                    }
def gui_init():
    #Mainwindows settings
    root.title('Kreator folderów R')
    root.maxsize(1920,1080)
    root.minsize(600,400)

    root_frame=Frame(root,bg=c_dark_grey)
    root_frame.pack(fill="both",expand=True)   

    Label(root_frame,
        text="Wybierz autora:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=0, padx=(5,5), pady=0, sticky="sew")

    type_combobox = ttk.Combobox(root_frame,
        foreground=c_black,  
        background=c_grey,
        values=[x for x in list(names_dict.keys())],
        height=20,state="readonly")
        
    type_combobox.current(0)
    type_combobox.grid(row=1,column=0,padx=(5,5), sticky="new")

    path = 'Radzyń 1'

    if not os.path.exists(path+'/Sebastian Mielczarek/'):
        os.makedirs(path+'/Sebastian Mielczarek/')

if __name__ == "__main__":
    gui_init()
    root.mainloop()
