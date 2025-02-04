#write a python program which used to drop the table using connection of oracle and write a query
#step1
import oracledb as orc
def drop():
    try:
        con_obj=orc.connect("system/1705@localhost/XE")
        cu=con_obj.cursor()
        q=input("write a query which u want to drop the table:")
        cu.execute(q)
        print("u had successfully drop the table please verify")
    except orc.DatabaseError:
        print("there is problem in your db please check it ")
drop()