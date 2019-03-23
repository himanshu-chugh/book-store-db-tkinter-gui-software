import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS BOOKS(id INTEGER PRIMARY KEY AUTOINCREMENT,TITLE VARCHAR(50),AUTHOR VARCHAR(50),YEAR INTEGER,ISBN INTEGER)")

    def insert(self,title,author,year,isbn):
        if(title!="" and author!="" and year!="" and isbn!=""):
            self.cur.execute("INSERT INTO BOOKS VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
            self.conn.commit()


    def delete(self,id):
        self.cur.execute("DELETE FROM BOOKS WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE BOOKS SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()



    def view(self):
        self.cur.execute("SELECT * FROM BOOKS")
        rows = self.cur.fetchall()
        return rows



    def search(self,title="",author="",year="",isbn="",logic="OR"):
        if(logic=="AND"):
            self.cur.execute("SELECT * FROM BOOKS where title=? AND author=? AND year=? AND isbn=? ",(title,author,year,isbn))
        else :
            self.cur.execute("SELECT * FROM BOOKS where title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows
    
    def close(self):
        try:
            self.conn.close()

        except Exception as e:
            print(e)
        exit()
    def __del__(self):
        self.conn.close()



