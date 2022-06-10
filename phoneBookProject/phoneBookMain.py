#!/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    this is Syntax to declare the encoding of a Python source file. It's discussed
    in PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
#
# Python Ver:   3.10.1
#
# Author:       Andrew f Weber
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#be sure to import the other modules
# we do this do have access/ functionality
import phoneBookFunc
import phoneBookGUI

# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(500,300) # Height is first, width second
        self.master.maxsize(500,300)
        # This centerwindow method will center our app on the user's screen
        phoneBookFunc.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # this protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner "X" on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: phoneBookFunc.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        #keeping your code comparmentalized and clutter free!
        phoneBookGUI.load_gui(self)

        #instantiate the tkinter menu dropdown object
        # This is the menu that will appear
        #menubar = Menu(self.master)
        #filemenu = Menu(menubar, tearoff=0)
        #filemenu.add_seperator()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
