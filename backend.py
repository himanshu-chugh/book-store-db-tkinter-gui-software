import sqlite3

def connect():
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BOOKS(id INTEGER PRIMARY KEY AUTOINCREMENT,TITLE VARCHAR(50),AUTHOR VARCHAR(50),YEAR INTEGER,ISBN INTEGER)")
    conn.commit()
    conn.close()

def delete_db():
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("drop table books")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BOOKS VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM BOOKS WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("UPDATE BOOKS SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOKS")
    rows = cur.fetchall()
    conn.close()
    return rows



def search(title="",author="",year="",isbn="",logic="OR"):
    conn = sqlite3.connect("gui.db")
    cur = conn.cursor()
    if(logic=="AND"):
        cur.execute("SELECT * FROM BOOKS where title=? AND author=? AND year=? AND isbn=? ",(title,author,year,isbn))
    else :
        cur.execute("SELECT * FROM BOOKS where title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows



connect()
"""
for i in range(5):
    insert("hellow","himanshu"+str(i),2019,45646)

print(view())

print("\n\n")
print(search(author='himanshu1'))
delete(id=1)
print("\n\n")
update(3,"dfid","Avfed",98,123)
print(view())

delete_db()
print(search(title="hellow"),"<<<<<<<<<<<<<<<<<<")
"""