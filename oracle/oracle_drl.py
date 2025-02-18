#write a python program which is used to print the one record and many record and all record
import oracledb as orc
def read():
    try:
        print("-"*50)
        con_obj=orc.connect("system/1705@localhost/XE")
        cu=con_obj.cursor()
        q=input("eneter the query:")
        cu.execute(q)
        # record=cu.fetchone()
        record = cu.fetchmany(0)
        record=cu.fetchall()
        print(record)
    except orc.DatabaseError as db:
        print("there is problem in b=",db)
read()