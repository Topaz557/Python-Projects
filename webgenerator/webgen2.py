import tkinter
from tkinter import filedialog
from tkinter import *
import webbrowser


#open and read the file after the appending:


### to create our next project we will need to import in a GUI that provides func
# to accomplish this we will do import "filename" and set the filename to write


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

    
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('HTML Box')
        self.master.config(bg='lightgray')

        
        self.lblDisplay = Label(self.master, text='Enter the text you wish to assign to the HTML', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblDisplay.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txt = Entry(self.master, text='', font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txt.grid(row=1, column=0, padx=(30,0), pady=(30,0))


        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
       

    def submit(self): # submit is class, self is method
        f = open("basicWebsite.html", "w")
        x = self.txt.get()# here we are assinging the variable to be what we type in above in the entry box
        f.write(x) # Here we are telling it to then write what was written in the box inside the html
        f.close() # this closes the HTML document so we stop making changes
        webbrowser.open_new_tab("basicWebsite.html") # This allows us to link into the webpage/ opens new tab to web browser
        
        
    def cancel(self): # this allows us to close program from GUI
        self.master.destroy()

    
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
