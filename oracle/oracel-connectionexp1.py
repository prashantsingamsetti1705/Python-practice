#write a python program of conection of oracle db
#step-1
import oracledb as orc
try:
    # step-1
    con_obj=orc.connect("system/1705@localhost/XE")
    print("oracle is connted sucessfully")
    print("type",type(con_obj))#type <class 'oracledb.Connection'>
except orc.DatabaseError:
    print("problem in oracle db")
