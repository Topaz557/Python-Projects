import tkinter
import webgen2.py
from tkinter import filedialog
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

    
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('HTML Box')
        self.master.config(bg='lightgray')

        self.txt = Entry(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txt.grid(row=1, column=0, padx=(30,0), pady=(30,0))


        self.lblDisplay = Label(self.master, text='Enter the text you wish to assign to the HTML', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblDisplay.grid(row=0, column=0, padx=(30,0), pady=(30,0))
       

    def submit(self): # submit is class, self is method
        fn = self.varFName.get() ## here we are creating a temp value to store the fname and lname
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {} !'.format(fn, ln))
        
    def cancel(self): 
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
