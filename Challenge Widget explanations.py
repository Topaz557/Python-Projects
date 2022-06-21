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
       
            
        self.varFName = StringVar()
        self.varLName = StringVar()
       
        self.lblFName = Label(self.master, text='First Name', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master, text='Last Name', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        # This is going to create our Button for Ask directory
        self.btnbrowse = Button(self.master, text="Browse", width=10, height=2, command=self.ask)
        self.btnbrowse.grid(row=4, column=0, padx=(0,0), pady=(30,0), sticky=NE)

        # This is going to create our box that allows for text entry for ask directory
        self.txtbrowse = Entry(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtbrowse.grid(row=4, column=1, padx=(30,0), pady=(30,0))

        
               
        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))


        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

                ## Note that we did the pad x at 90 on the second x var. we did this because if we make it 90 on
                # the row prior we will cover our submit button. Keep an eye on these going forward for correct placement

    def submit(self): # submit is class, self is method
        fn = self.varFName.get() ## here we are creating a temp value to store the fname and lname
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {} !'.format(fn, ln))
        
    def cancel(self): 
        self.master.destroy()

    # The delete method for self is what allows us to not have duplicates in browse gui
    def ask(self):
        self.txtbrowse.delete(0,END)
        x = tkinter.filedialog.askdirectory() # This opens the actual file expolorer 
        self.txtbrowse.insert(0,x)
        ## the self. txt browse insert is what puts the file path into the browse
        
# cancel is class, self is method

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
