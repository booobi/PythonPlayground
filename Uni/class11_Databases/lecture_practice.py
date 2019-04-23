import sqlite3

db_name = "blablaDB.db"

conn = sqlite3.connect(db_name)
curs = conn.cursor()
curs.execute("Create table IF NOT EXISTS Customers(firstCol TEXT)")
curs.execute("INSERT INTO Customers values('test')")
curs.execute("select * from Customers")
# conn.commit()
print curs.fetchone()
curs.close()
conn.close()

conn = sqlite3.connect(db_name)
curs = conn.cursor()
# Previous connection has to be commited!
curs.execute("select * from Customers")
print curs.fetchone()

print curs.connection
print sqlite3.apilevel
