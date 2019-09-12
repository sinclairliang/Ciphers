import tkinter
from tkinter import *




def testFunction():
    print("Hello World")

window = tkinter.Tk()
pathStr = StringVar()
window.title("Book Cipher")
tkinter.Label(window, text="Path of the message").grid(row=0)
path = Entry(window).grid(row=0, column=1)

tkinter.Label(window, text="Path of the key").grid(row=1)
tkinter.Entry(window).grid(row=1, column=1)

tkinter.Button(window, text="Enter").grid(row=2)

textArea0 = tkinter.Text(window, height=10, width=20, highlightcolor="green", highlightthickness=1, borderwidth=1, relief="groove").grid(row=3)

window.mainloop()