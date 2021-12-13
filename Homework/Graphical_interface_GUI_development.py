# Create an application with a graphical interface that:
# • Have a box labeled "Enter name" where the user can enter a name
# • Have a button labeled "Confirm" that, when pressed, will cause the program to print "Hello {name}!" Below the field.
# • Print a greeting not only by pressing the button, but also by pressing the "Enter" button
# • There would be a "Clear" item, which would delete the text on the line where the greeting text is printed.
# • There would be a "Restore" item, which, when clicked, would print the last printed text in the welcome text line
# • There would be an "Exit" item, which would close the program window
# • There would be a separator line between the "Restore" and "Exit" menu items
# • "Created" would be displayed when the greeting text is printed
# • "Cleared" is displayed when the greeting text is deleted
# • "Playback" is displayed when the last greeting text is played. Pressing the "Escape" key on the keyboard closes
# program window

from tkinter import *

win = Tk()
last = StringVar()


def greeting():
    inp = inp1.get()
    lbl2["text"] = f"Hello, {inp}!"
    last.set(lbl2["text"])
    status["text"] = "Created"


def clear():
    lbl2["text"] = ""
    status["text"] = "Clear"


def restore():
    lbl2["text"] = last.get()
    status["text"] = "Restored"


def close():
    win.destroy()


lbl1 = Label(win, text="Enter name")
inp1 = Entry(win)
btn1 = Button(win, text="Confirm", command=greeting)
inp1.bind("<Return>", lambda event: greeting())
lbl2 = Label(win, text="")
win.bind("<Escape>", lambda event: close())


status = Label(win, text="", bd=1, relief=SUNKEN, anchor=W)

lbl1.grid(row=0, column=0)
inp1.grid(row=0, column=1)
btn1.grid(row=0, column=2)
lbl2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)

meniu = Menu(win)
win.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Clear", command=clear)
submeniu.add_command(label="Playback", command=restore)
submeniu.add_separator()
submeniu.add_command(label="Exit", command=close)

win.mainloop()
