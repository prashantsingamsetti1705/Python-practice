#here we hae to read add the empolye data
import pickle
#here programmer defined exception
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLenghtError(Exception):pass
#hitting the programmer dif exception
def val(name:str):
    if name==0:
        raise ZeroLenghtError
    elif name.isspace():
        raise SpaceError
    else:
        wodrs=name.split()
        res=True
        for word in wodrs:
            if not word.isalpha():
                res=False
        if res:
            return name
        else:
            raise InvalidNameError
#

def addEmp():
    with open("emp.text", "ab") as fp:
        while True:
            try:
                print("-"*50)
                eno=int(input("ENTER THE EMPLOYEE NUMBER:"))
                en=val(input("ENTER THE EMPLOYEE NAME:"))
                esal=float(input("ENTER THE EMPLOYEE SALARY:"))
                print("-" * 50)
                lst=[]
                lst.append(eno)
                lst.append(en)
                lst.append(esal)
                pickle.dump(lst,fp)
                print("-"*100)
                print("FILE SAVED SUCCESSFULLY")
                ch=input("do you want to enter data (yes/no)")
                if ch.lower()=="no":
                    print("thanks for using this program")
                    break
            except ValueError:
                print("dont enter the alpha numeric for esal")
            except InvalidNameError:
                print("dont enter the alpha numerics for eno/en")
            except SpaceError:
                print("dont enter the space for eno/en")
            except ZeroLenghtError:
                print("dont enter empty for eno/en")

