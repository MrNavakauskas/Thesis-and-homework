from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
import sqlite3
# import a

class SqlLangas():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="light blue", height=1024, width=1024)  # this is the background
        self.frame.pack(fill="both", expand="true", anchor="c")
        master.geometry("626x431")
        master.resizable(0, 0)
        master.title("Čia bus naudojama SQL duombazė COVID-19 registrui")
        master.iconbitmap(r'covidicon.ico')
        self.frame_login = tk.Frame(master, bg="light grey", relief="groove", bd=2)  # prisijungimo detales/mygtukai...
        self.frame_login.place(rely=0.30, relx=0.17, height=120, width=400)
        # button = tk.Button(master, fg='red', text="Pradėti", width=10, command=lambda: pradeti())
        # button.place(rely=0.80, relx=0.75)

# def pradeti():
#     a.main()

def main():
    root = tk.Tk()
    app = SqlLangas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
