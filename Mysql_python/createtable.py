#write a python program which create a table
import mysql.connector as sql
try:
    con=sql.connect(host="localhost",user="root",passwd="1705",database="employees")
    cu=con.cursor()
    qt=input("enter the query to create a table")
    cu.execute(qt)
    print("the tbale is created sucessfully --->verify")
except sql.DatabaseError as db:
    print("ther is problem in your db -->verify it =",db)
