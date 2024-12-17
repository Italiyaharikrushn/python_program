#Import required libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of the window
win.geometry("750x250")

#Define a function to show the messagebox
def handler():
   messagebox.showinfo("Message", "You have clicked a Button")

#Create a Label
Label(win, text= "Click the below button", font=('Helvetica 16 underline')).pack(pady=20)

#Create a Button
ttk.Button(win, text= "Click", command= handler).pack(pady=30)
win.mainloop()