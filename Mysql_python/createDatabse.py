#write a python programwhich is used create databse
#step-1 importing the module
import mysql.connector as sql
try:
    #step-2 connecting the sql
    con_obj=sql.connect(host="localhost",user="root",passwd="1705")
    #step-3 create the cursor
    cu=con_obj.cursor()
    #step-4 writing the query
    q=input("enter the databse name which you to create:")
    #step-5 executing the query
    cu.execute(q)
    print("your databse created sucessfully please--->verify")
except sql.DatabaseError as db:
    print("their is a problem in your db--->verify:",db)

