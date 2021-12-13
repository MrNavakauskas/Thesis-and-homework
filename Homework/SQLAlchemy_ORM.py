# Create an application that:
# • Data is stored in a database using SQLAlchemy ORM (without SQL queries)
# • Has to have a graphical interface (with icon and name). Create via Tkinter
# • Allow to enter persons in the database (their name, surname, age, ...)
# • Displays a list of all persons entered in the database
# • Allows you to delete the selected person from the database
# • Allows you to edit the data of the entered person and save the updates to the database


from SQLAlchemy_ORM_dbcon import *
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, SINGLE, END

person_edit = False
get_all_records_list()


def update_fields():
    box.delete(0, END)
    box.insert(END, *get_all_records_list())
    field1.delete(0, 'end')
    field2.delete(0, 'end')
    field3.delete(0, 'end')
    field1.focus()


def ui_add(event):
    global person_edit
    if person_edit:
        update_record(person_edit.id, field1.get(), field2.get(), field3.get())
        person_edit = False
    else:
        add_record(field1.get(), field2.get(), field3.get())
    update_fields()


def ui_delete():
    active = get_all_records_list()[box.curselection()[0]]
    delete_record(active.id)
    update_fields()


def ui_edit():
    global person_edit
    person_edit = get_all_records_list()[box.curselection()[0]]
    update_fields()
    field1.insert(0, person_edit.name)
    field2.insert(0, person_edit.surname)
    field3.insert(0, person_edit.age)

# Graphic Objects initialization
main_window = Tk()
main_window.title("Person catalog")
main_window.iconbitmap('1.ico')
# main_window.iconbitmap(r'1.ico')
top_frame = Frame(main_window)
btn_frame = Frame(main_window)
box = Listbox(btn_frame, selectmode=SINGLE)
box.insert(END, *get_all_records_list())
note1 = Label(top_frame, text="Insert person", width=40)
field1 = Entry(top_frame)
field1_lb = Label(top_frame, text="Name")
field2 = Entry(top_frame)
field2_lb = Label(top_frame, text="Surname")
field3 = Entry(top_frame)
field3_uzr = Label(top_frame, text="Age")
btn1 = Button(top_frame, text="Add")
btn1.bind("<Button-1>", ui_add)
field1.bind("<Return>", ui_add)
field2.bind("<Return>", ui_add)
field3.bind("<Return>", ui_add)
btn2 = Button(top_frame, text="Edit", command=ui_edit)
btn3 = Button(top_frame, text="Delete", command=ui_delete)

# Graphic Objects visualization
note1.grid(row=0, columnspan=2)
field1_lb.grid(row=1, column=0)
field1.grid(row=1, column=1)
field2_lb.grid(row=2, column=0)
field2.grid(row=2, column=1)
field3_uzr.grid(row=3, column=0)
field3.grid(row=3, column=1)
btn1.grid(row=4, columnspan=2, sticky="E")
btn2.grid(row=4, columnspan=2)
btn3.grid(row=4, columnspan=2, sticky="W")
box.pack()
top_frame.pack()
btn_frame.pack()
main_window.mainloop()
