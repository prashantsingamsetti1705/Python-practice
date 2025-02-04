#write a python program which is used to update the record from table
import mysql.connector as sql
try:
    con=sql.connect(host="localhost",user="root",passwd="1705",database="employees")
    cu=con.cursor()
    q=input("enter the query wchich you want to update it:")
    cu.execute(q)
    con.commit()
    if cu.rowcount>0:
        print("the record is update please--verify it")
    else:
        print("yhe record is empty")
except sql.DatabaseError as db:
    print("thier is problem in dn please---verify it=",db)