#write a python program which is used to insert the value by connection oracle db
#robast program
#using the excepiton abd etc
#name valid exception error
import oracledb as orc
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLenghtError(Exception):pass
def val(name:str):
    if len(name)==0:
        raise ZeroLenghtError
    elif name.isspace():
        raise SpaceError
    else:
        words=name.split()#words
        res=True
        for word in words:
            if not word.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvalidNameError
#
def insert():
    while True:
        try:
            #step-2
            con_obj=orc.connect("system/1705@localhost/XE")
            #step-3
            cu=con_obj.cursor()
            eno=int(input("enter your employee number eno:"))
            en=val(input("enter the employess name:"))
            esal=float(input("eneter the employee sal :"))
            ecompany=val(input("eneter your company name:"))
            #step-4
            q="insert into empolyess values(%d,'%s',%f,'%s')"%(eno,en,esal,ecompany)
            cu.execute(q)
            #step-5
            con_obj.commit()
            print("values are inserted sucessfully")
            ch=input("do want enter the another records into data(yes/no)")
            if ch.lower()=="no":
                print("tanks for using this program")
                break
        except ValueError:
            print("dont eneter the alpha numercis")
        except ZeroLenghtError:
            print("dont not leve try to leave it")
        except InvalidNameError:
            print("dont not enter alpha numeric")
        except SpaceError:
            print("donot enter sapce for en,ecompany")
        except orc.DatabaseError as db:
            print("there is problem in orcale db=",db)
#main program
insert()#callin the function
