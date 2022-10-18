#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      aarus
#
# Created:     14-09-2022
# Copyright:   (c) aarus 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

gui = Tk(className='Window')
# set window size
gui.geometry("400x600")

#set window color
gui.configure(bg='pink')

def showMsg():
    messagebox.showinfo('Life is beautiful')

def close():
    gui.destroy()

Label(gui,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)
password = Entry(gui,show="*",width=20)
password.pack()


button = Button(gui,	text = 'Submit',	command = showMsg, bg='green', fg='red')
button.pack()

gui.mainloop()
