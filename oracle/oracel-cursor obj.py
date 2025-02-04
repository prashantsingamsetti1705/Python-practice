#write a python program which is used to ctect the data base and create the data base
import oracledb as orc
try:
    con_obj=orc.connect("system\1705@localhost\XE")
    print("oracle is connnted sucessfully plese verif")
    cu=con_obj.cursor()
    print("corser is connetd sucessfuly")
except orc.DatabaseError:
    print("there is problem in oracle db plrse check it")