# Create an application that:
# • Create a database
# • Create a table of lectures with columns title, teacher and duration
# • Create three lectures: (‘Management’, ‘Gediminas’, 40), (‘Python’, ‘John’, 80) and (‘Java’, ‘Tom’, 80)
# • Print only lectures which are longer than 50
# • Update the title of the lecture "Python" to "Python Programming"
# • Delete a lecture where teacher is Tom
# • Print all lectures (full table)

import sqlite3

conn = sqlite3.connect("lectures.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS lectures (
            name text,
            teacher text,
            duration integer
            )""")

with conn:
    c.execute("INSERT INTO lectures VALUES ('Management', 'Gediminas', 40)")
    c.execute("INSERT INTO lectures VALUES ('Python', 'John', 80)")
    c.execute("INSERT INTO lectures VALUES ('Java', 'Tom', 80)")

with conn:
    c.execute("SELECT * From lectures Where duration > 50")
    print(c.fetchall())

with conn:
    c.execute("UPDATE lectures SET name='Python Programming' WHERE name='Python'")

with conn:
    c.execute("DELETE from lectures WHERE teacher='Tom'")

with conn:
    c.execute("SELECT * From lectures")
    print(c.fetchall())
