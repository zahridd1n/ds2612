
import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    son INTEGER,
    narx REAL
    )
""")
conn.commit()

c.execute("""
    INSERT INTO products(id,name,son,narx)
    VALUES(3,"Olma",1000,3500)
""")
conn.commit()

