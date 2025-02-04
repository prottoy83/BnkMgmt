import sqlite3

con =sqlite3.connect("bankdb.db")
cur = con.cursor()

def dbConnect():
    for row in cur.execute("SELECT * FROM users"):
        print(row)


dbConnect()