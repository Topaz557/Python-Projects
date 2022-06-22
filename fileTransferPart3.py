import shutil
import os
from datetime import timedelta
import datetime
import time
import tkinter
from tkinter import filedialog
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

    
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinters')
        self.master.config(bg='lightgray')
       
      
       
        self.lblSource = Label(self.master, text='Source', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblSource.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLDestination = Label(self.master, text='Destination', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblLDestination.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        

        self.txtSource = Entry(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtSource.grid(row=0, column=1, padx=(30,0), pady=(30,0))

    
        self.txtDestination = Entry(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtDestination.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        
        # This is going to create our Button for Ask directory
        self.btnSource = Button(self.master, text="Browse", width=10, height=2, command=self.ask)
        self.btnSource.grid(row=0, column=2, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnDestination = Button(self.master, text="Browse", width=10, height=2, command=self.ask2)
        self.btnDestination.grid(row=1, column=2, padx=(0,0), pady=(30,0), sticky=NE)

    
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

                ## Note that we did the pad x at 90 on the second x var. we did this because if we make it 90 on
                # the row prior we will cover our submit button. Keep an eye on these going forward for correct placement

    def submit(self):
        source = self.txtSource.get()
        destination = self.txtDestination.get()
        files = os.listdir(source)
        for i in files:
            time2 = datetime.datetime.now()
            job = os.path.join(source, i)
            var = time2 - timedelta(hours = 24)
            time = os.path.getmtime(job)
            ftime = datetime.datetime.fromtimestamp(time)    
            if var < ftime:
                shutil.move(source + '/' + i, destination)
                
        
    def cancel(self): 
        self.master.destroy()


    def ask(self):
        self.txtSource.delete(0,END)
        x = tkinter.filedialog.askdirectory() # This opens the actual file expolorer 
        self.txtSource.insert(0,x)

    def ask2(self):
        self.txtDestination.delete(0,END)
        x = tkinter.filedialog.askdirectory() # This opens the actual file expolorer 
        self.txtDestination.insert(0,x)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



#set where the source of the files are
