import tkinter
from tkinter import *
from tkinter import messagebox


        self.lblFName = Label(self.master, text='First Name', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

        self.lblLName = Label(self.master, text='Last Name', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblLName.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

        self.lblPhone = Label(self.master, text='Phone Number', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblPhone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

        self.lblEmail = Label(self.master, text='Email Address', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblEmail.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

        self.lblInfo = Label(self.master, text='Information:', font=("Helvetica", 16),fg='black', bg='lightgray')
        self.lblInfo.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)




        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtFName.grid(row=1, column=0, padx=(30,0), pady=(30,0), sticky=N+W)


        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16),fg='black', bg='lightblue')
        self.txtLName.grid(row=3, column=0, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
