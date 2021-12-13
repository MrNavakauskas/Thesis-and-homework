from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
import sqlite3


def update(rows):
    tr_view.delete(*tr_view.get_children())
    for i in rows:
        tr_view.insert("", "end", values=i)


def find():
    s2 = s.get()
    query1 = "SELECT id, name, surname, age, vaccination FROM vaccination_TB WHERE name LIKE '%"+s2+"%' " \
                            "OR surname LIKE '%"+s2+"%' OR age LIKE '%"+s2+"%' OR vaccination LIKE '%"+s2+"%'"
    cursor.execute(query1)
    rows = cursor.fetchall()
    update(rows)


def return_db():
    query = "SELECT id, name, surname, age, vaccination FROM vaccination_TB"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

# 2 click get data
def insert(event):
    item = tr_view.item(tr_view.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])


def update_and():
    id1 = t1.get()
    nm = t2.get()
    srn = t3.get()
    ag = t4.get()
    vacc = t5.get()
    query = "UPDATE vaccination_TB SET name = ?, surname = ?, age = ?, vaccination = ? WHERE id = ?"
    cursor.execute(query, (nm, srn, ag, vacc, id1))
    database.commit()
    return_db()


def add_new():
    id1 = t1.get()
    nm = t2.get()
    srn = t3.get()
    ag = t4.get()
    vacc = t5.get()
    query = "INSERT INTO vaccination_TB (id, name, surname, age, vaccination) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (id1, nm, srn, ag, vacc))
    database.commit()
    return_db()


def delete_id():
    ir_id = t1.get()
    query = "DELETE FROM vaccination_TB WHERE id = " + ir_id
    cursor.execute(query)
    database.commit()
    return_db()


database = sqlite3.connect("database6.db")
cursor = database.cursor()

root = Tk()
s = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()

sektor1 = LabelFrame(root, text="Vaccination list")
sektor2 = LabelFrame(root, text="Values")
sektor3 = LabelFrame(root, text="Data")
sektor1.pack(fill="both", expand="yes", padx=20, pady=10)
sektor2.pack(fill="both", expand="yes", padx=20, pady=10)
sektor3.pack(fill="both", expand="yes", padx=20, pady=10)

tr_view = ttk.Treeview(sektor1, columns=(1, 2, 3, 4, 5), show="headings", height="10")
tr_view.pack()

tr_view.heading(1, text="Nr.", anchor="w")
tr_view.heading(2, text="Name", anchor="w")
tr_view.heading(3, text="Surname", anchor="w")
tr_view.heading(4, text="Age", anchor="w")
tr_view.heading(5, text="Vaccine nr.", anchor="w")

tr_view.bind('<Double 1>', insert)

query = "SELECT * FROM vaccination_TB"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

lbl_sek2 = Label(sektor2, text="Search")
lbl_sek2.pack(side=tk.LEFT, padx=10)
ent_sek2 = Entry(sektor2, textvariable=s)
ent_sek2.pack(side=tk.LEFT, padx=6)
btn_sek2a = Button(sektor2, text="Search", command=find)
btn_sek2a.pack(side=tk.LEFT, padx=6)
btn_sek2b = Button(sektor2, text="Back", command=return_db)
btn_sek2b.pack(side=tk.LEFT, padx=6)

lbl1_sek3 = Label(sektor3, text="Id")
lbl1_sek3.grid(row=0, column=0, padx=5, pady=3)
ent_sek3 = Entry(sektor3, textvariable=t1)
ent_sek3.grid(row=0, column=1, padx=5, pady=3)

lbl2_sek3 = Label(sektor3, text="Name")
lbl2_sek3.grid(row=1, column=0, padx=5, pady=3)
ent2_sek3 = Entry(sektor3, textvariable=t2)
ent2_sek3.grid(row=1, column=1, padx=5, pady=3)

lbl3_sek3 = Label(sektor3, text="Surname")
lbl3_sek3.grid(row=2, column=0, padx=5, pady=3)
ent3_sek3 = Entry(sektor3, textvariable=t3)
ent3_sek3.grid(row=2, column=1, padx=5, pady=3)

lbl4_sek3 = Label(sektor3, text="Age")
lbl4_sek3.grid(row=3, column=0, padx=5, pady=3)
ent4_sek3 = Entry(sektor3, textvariable=t4)
ent4_sek3.grid(row=3, column=1, padx=5, pady=3)

lbl5_sek3 = Label(sektor3, text="Vacc.nr.")
lbl5_sek3.grid(row=4, column=0, padx=5, pady=3)
ent5_sek3 = Entry(sektor3, textvariable=t5)
ent5_sek3.grid(row=4, column=1, padx=5, pady=3)

btn_sek3a = Button(sektor3, text="Update", command=update_and)
btn_sek3a.grid(row=5, column=0, padx=5, pady=3)
btn_sek3b = Button(sektor3, text="Add", command=add_new)
btn_sek3b.grid(row=5, column=1, padx=5, pady=3)
btn_sek3c = Button(sektor3, text="Delete", command=delete_id)
btn_sek3c.grid(row=5, column=2, padx=5, pady=3)


root.geometry("1050x540")
root.resizable(0, 0)
root.title("COVID19 database")
root.iconbitmap(r'1.ico')

root.mainloop()
