#write a python programm which  is to connecthe the mysql database
#step-1
import mysql.connector as sql
try:
    #step-2
    con_obj=sql.connect(host="localhost",user="root",passwd="1705")

    print("your databse connected sucessfully--->verify")

except sql.DatabaseError as db:
    print("there is problem in your databse plese check it{}".format(db))

