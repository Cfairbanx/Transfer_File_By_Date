
import tkinter as tk
from tkinter import *
from tkinter import filedialog 
import shutil
import os
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True,height=True)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Check Files')
        self.master.config(bg='#F9EBEA')

        self.var_dir = StringVar()
        self.var_dir1 = StringVar()
        
#text boxs
        self.txtBrowse = Entry(self.master,text=self.var_dir, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse.grid(row=1, column=1, columnspan=3, padx=(30,0),pady=(30,0))

        self.txtBrowse1 = Entry(self.master,text=self.var_dir1, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=2, column=1, columnspan=3, padx=(30,0),pady=(30,0))
        
        self.btnBrowse = Button(self.master,text = "Browse...", width=12,height=1,command=self.source_dir)
        self.btnBrowse.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky=NW)

        self.btnBrowse1 = Button(self.master,text = "Browse...", width=12,height=1,command=self.dest_dir)
        self.btnBrowse1.grid(row=2,column=0,padx=(30,0),pady=(30,0),sticky=NW)

        self.btnCheckfor = Button(self.master,text = "Check for files...", width=12,height=2,command=self.move_files)
        self.btnCheckfor.grid(row=3,column=0,padx=(30,0),pady=(30,0),sticky=SW)

        self.btnClose = Button(self.master,text = "Close Program", width=12,height=2,command=self.cancel)
        self.btnClose.grid(row=3,column=3,padx=(0,0),pady=(0,0),sticky=SE)
        
#Button functionality
    def source_dir(self):
        source = tk.filedialog.askdirectory()
        self.txtBrowse.delete(0,END)
        self.txtBrowse.insert(0,source)
        
    def dest_dir(self):
        source = tk.filedialog.askdirectory()
        self.txtBrowse1.delete(0,END)
        self.txtBrowse1.insert(0,source)
        
    def move_files(self):
        local = datetime.now() - timedelta(hours = 24)
        source = self.txtBrowse.get()
        destination = self.txtBrowse1.get()
        files = os.listdir(source)
        for i in files:
            absolutepath = os.path.join(source,i)
            modTimes = os.path.getmtime(absolutepath)
            Mtime = datetime.fromtimestamp(modTimes)

            if Mtime > local:
                shutil.move(absolutepath, destination)
        
    
        
    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
