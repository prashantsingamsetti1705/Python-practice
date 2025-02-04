#write a python program which used to drop a database
import mysql.connector as sql
try:
    con=sql.connect(host="localhost",user="root",passwd="1705",database="student")
    cu=con.cursor()
    q=input("enter the query which you want to drop the database")
    cu.execute(q)
    print("the data base is drop sucessfully--->verify it")
except sql.DatabaseError as db:
    print("thier is problem in your databse please --->verify:",db)