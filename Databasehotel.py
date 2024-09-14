import sqlite3

def hotelData():
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS booking (id INTEGER PRIMARY KEY, CusID text, Firstname text, Surname text, \
     Address text, Gender text, Mobile text, Nationality text, ProveOfID text, DateIn text, DateOut text, Email text)")
    con.commit()
    con.close()


def addHotelRec(CusID, Firstname, Surname, Address, Gender, Mobile, Nationality, ProveOfID, DateIn, DateOut, Email):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("INSERT INTO booking (CusID, Firstname, Surname, Address, Gender, Mobile, Nationality, ProveOfID, DateIn, DateOut, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (CusID, Firstname, Surname, Address, Gender, Mobile,Nationality,ProveOfID, DateIn,DateOut, Email))
    con.commit()
    con.close()



def viewData():
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM booking")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("DELETE FROM booking WHERE id=?",
                (id,))
    con.commit()
    con.close()


def searchData(CusID="", Firstname="", Surname="", Address="", Gender="", Mobile="", Nationality="", ProveOfID="",
               DateIn="", DateOut="", Email=""):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM booking WHERE CusID=? OR Firstname=? OR Surname=? OR Address=? OR Gender=? OR Mobile=?  \
        OR Nationality=? OR ProveOfID=? OR DateIn=? OR DateOut=? OR Email=?",
        (CusID, Firstname, Surname, Address, Gender, Mobile, Nationality, ProveOfID, DateIn, DateOut, Email))
    rows = cur.fetchall()
    con.close()
    return rows


