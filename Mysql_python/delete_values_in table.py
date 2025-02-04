#write a python program which is used to delte the values in table;
import mysql.connector as sql
try:
     con=sql.connect(host="localhost",user="root",passwd="1705",database="employees")
     cu=con.cursor()
     q=input("enter the query which u want to delete it:")
     cu.execute(q)
     con.commit()
     print("the recor is delted please verify--->it{}".format(cu.rowcount))
except sql.DatabaseError as db:
    print("their is problem in your db plese check it {}".format(db))


