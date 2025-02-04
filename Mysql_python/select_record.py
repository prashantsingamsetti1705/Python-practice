#write a python program wchich is used to select table and show the all records
import mysql.connector as sql
try:
    con=sql.connect(host="localhost",user="root",passwd="1705",database="employees")
    cu=con.cursor()
    q=input("enter the quer whcih you want show the record")
    cu.execute(q)
    record=cu.fetchall()
    for records in record:
        for val in records:
            print(val,end="\t\t")
        print()
except sql.DatabaseError:
    print("their is problem in your racle please check it---verify")