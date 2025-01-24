# Program for Reading Employee Deatils and save then File by using Pickling Concpt
# EmpPickEx1.py
class ZerolengthError(Exception):pass
class InvalidnameError(Exception):pass
class SpaceError(Exception):pass
def val(name:str):
    if len(name)==0:
        raise ZerolengthError
    elif name.isspace():
        raise SpaceError
    else:
        words=name.split()
        res =True
        for word in words:
            if (not word.isalpha()):
                res=False
                break
        if res:
            return name
        else:
            raise InvalidnameError



import pickle
def pk():
    while True:
        with open("emp.txt","ab") as fp:
            print("*"*50)
            #here empoplye deatails
            try:
                eno=int(input("enter the emp number:"))
                en=val(input("enter the emp name:"))
                es=float(input("enter the emp salary:"))
                ed=val(input("enter the emp disignation:"))
                # create an empty list and the place the above values
                lst=[]
                lst.append(eno)
                lst.append(en)
                lst.append(es)
                lst.append(ed)
                pickle.dump(lst,fp)
                print("*"*50)
                print("file saved sucessfully")
                ch=input("du want to enter the the empa data:")
                if ch=="no":
                    print("thanks for using this program")
                    break
            except ValueError:
                print("dont enter the alpha numeric")
            except InvalidnameError:
                print("dont eter the al numeric for en/ed")
            except ZerolengthError:
                print("dont fill the empty")
            except SpaceError:
                print("dont enter the space"
                      "")
pk()
