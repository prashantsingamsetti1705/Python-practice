#write a python program which is used insert the values into the table
#genrating name valid exception
class InvalidNameError(Exception):pass
class ZerolenghtError(Exception):pass
class SpaceError(Exception):pass
def val(name:str):
    if len(name)<=0:
        raise ZerolenghtError
    elif name.isspace():
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if not word.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvalidNameError
import mysql.connector as sql
while True:
    try:
        con=sql.connect(host="localhost",user="root",passwd="1705",database="employees")
        cu=con.cursor()
        eno=int(input("enter the en number:"))
        ename=val(input("enter the ename:"))
        esal=float(input("enter the employees sal:"))
        ecompany=val(input("enter trhe company name"))
        q="insert into emp values(%d,'%s',%f,'%s')"%(eno,ename,esal,ecompany)
        cu.execute(q)
        con.commit()
        print("the values are inerted sucessfully please verify--it{}",cu.rowcount)
        ch=input("do u want to enetr the values or (yes or not)")
        if ch.lower()=="no":
            print("thanks for using this program")
            break
    except ValueError:
        print("do not enter alapha num")
    except InvalidNameError:
        print("do not enter thealpha numerisc for ename.ecompany")
    except SpaceError:
        print("do not eneter space for ename,ecompany")
    except ZerolenghtError:
        print("do not let it empty")
    except sql.DatabaseError as db:
        print("their is problem in your databse-->please check it=",db)




