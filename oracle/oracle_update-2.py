import oracledb as orc
def update2():
    while True:
        try:
            print("-"*50)
            con_obj=orc.connect("system/1705@localhost/XE")
            cu=con_obj.cursor()
            eno=int(input("enter the empolye numebre:"))
            esal=float(input("enter the employess sal:"))
            ecompany=input("enter the company name:")
            uq="update empolyess set esal=%f,ecompany='%s' where eno=%d"
            cu.execute(uq %(esal,ecompany,eno))
            con_obj.commit()
            if cu.rowcount>0:
                print("the sal is updated plese verify{}".format(cu.rowcount))
            else:
                print("ther is empty record in your table")
                print("-"*50)
            ch=input("enetr you u wnt o upadte or not(yes/no)")
            if ch.lower()=="no":
                print("thanks for using this program")
                break
        except orc.DatabaseError as db:
            print("their is problem in your db pelase verify --->",db)
update2()


