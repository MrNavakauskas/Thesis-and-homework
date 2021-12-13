from tkinter import *
import tkinter as tk
import next1

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("G.Navakauskas PT11 course work - COVID19 database")
root.eval('tk::PlaceWindow . center')
img = PhotoImage(file="covidPNG.png")
label = Label(root, image=img)
label.place(x=0, y=0)
button = tk.Button(root, fg='red', text="Begin", width=10, command=lambda: begin())
button.place(rely=0.80, relx=0.75)


def begin():
    root.destroy()
    next1.main()

root.mainloop()
