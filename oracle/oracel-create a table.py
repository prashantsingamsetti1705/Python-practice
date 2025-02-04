#write a python program which is used to create a table
#step1
from platform import system

import oracledb as orc
#setp2 to connection of oracle db
try:
    con_obj=orc.connect("system/1705@localhost/XE")
    #step3
    cu=con_obj.cursor()
    #step write a query
    q="create table emplo(eno number(2) primary key,en varchar2(10) not null,esal number(5,6) not null)"
    cu.execute(q)
    print("table is created sucessfully---->verify")

except orc.DatabaseError:
    print("their is a problem in orcale db please check it ")

#by dynamicly
import oracledb as orc
def create():
    try:
        con_obj=orc.connect("system/1705@localhost/XE")
        cu=con_obj.cursor()
        q=input("enter the query of create a table name--->:")
        cu.execute(q)
        print("table is created successfully ----->verify")
    except orc.DatabaseError:
        print("thier is a problem in oracle db please check it ")
create()