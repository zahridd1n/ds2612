import sqlite3

conn = sqlite3.connect("studens.db")
c = conn.cursor()

##jadval yaratish
c.execute("""
    CREATE TABLE student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    years INTEGER
    )
""")
conn.commit()

#Malumot qo'shish
c.execute("""
INSERT INTO student(id,name,class,years)
VALUES (1,"ali", "8a",2012)
""")
conn.commit()

##Malumot olish
c.execute("SELECT * FROM student")
a = c.fetchall()
for i in a:
    print(i)

c.execute("SELECT * FROM student WHERE id=2")
a = c.fetchall()
for i in a:
    print(i)

#Update qilish
c.execute("""
    UPDATE student SET name="Mahmudjon" WHERE id=2
""")
conn.commit()

#Delete 
c.execute("DELETE FROM student WHERE id=1")
conn.commit()


