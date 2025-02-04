import sqlite3

con = sqlite3.connect("bankdb.db")
cur = con.cursor()



def compUsername(usrname):
    result =  cur.execute("SELECT id FROM users WHERE username=:usn", {"usn": usrname}).fetchone()
    if result:
        return result[0]
    else:
        return 0

def getInfo(usrID):
    name = cur.execute("SELECT name FROM users WHERE id=:id", {"id": usrID}).fetchone()
    address = cur.execute("SELECT address FROM users WHERE id=:id", {"id": usrID}).fetchone()
    contact = cur.execute("SELECT contact FROM users WHERE id=:id", {"id": usrID}).fetchone()
    
    return name[0], address[0], contact[0]

compUsername("prottoy83")