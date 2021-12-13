import sqlite3

conn = sqlite3.connect("database6.db")
c = conn.cursor()

c.execute("""Create table if not exists vaccination_TB (Id integer, Name text, Surname text, age text,
Vaccination integer)""")

with conn:
    c.execute("INSERT INTO vaccination_TB VALUES ('1', 'Domas', 'Domaitis', '28', '1')")
    c.execute("INSERT INTO vaccination_TB VALUES ('2', 'Adomas', 'Adomaitis', '45', '3')")
    c.execute("INSERT INTO vaccination_TB VALUES ('3', 'Mykolas', 'Mykoliunas', '32', '2')")
    c.execute("INSERT INTO vaccination_TB VALUES ('4', 'Jonas', 'Janonis', '45', '2')")
    c.execute("INSERT INTO vaccination_TB VALUES ('5', 'Petras', 'Petrauskas', '32', '3')")
