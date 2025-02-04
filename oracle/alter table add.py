#wite a python program which to alter the table and add the data
#step 1
import oracledb as orc
def alteradd():
    try:
        con_obj=orc.connect("system/1705@localhost/XE")
        cu=con_obj.cursor()
        q=input("enter the query which u want to add in table:")
        cu.execute(q)
        print("db is conneted suecssfully----verify")
    except orc.DatabaseError:
        print("there is problem in the db --->please checkit ")
alteradd()