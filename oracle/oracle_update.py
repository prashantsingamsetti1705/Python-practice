#write a python program which is update the record of the data conntection pdbc by wrirting the query
import oracledb as orc
def update():
    try:
        con_obj=orc.connect("system/1705@localhost/XE")
        cu=con_obj.cursor()
        uq="update empolyess set esal=33.0,ecompany='tcs' where eno=200"
        cu.execute(uq)
        con_obj.commit()
        print("the sal is updated plese verify{}",cu.rowcount)
    except orc.DatabaseError as db:
        print("their is problem in your db pelase verify --->",db)
update()
