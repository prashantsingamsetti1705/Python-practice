#write a python program which will print the keyword verabel length
# def fdisp_kvl(id,sname,deg,**pra):
#     print("*"*50)
#     print("enter the studentid --->{}".format(id))
#     print("enter the studentsname --->{}".format(sname))
#     print("enter the studentclass --->{}".format(deg))
#     print("*"*50)
#     if len(pra)!=0:
#         tot=0
#         for sub,marks in pra.items():
#             print("sub-->{},marks------->{}".format(sub,marks))
#             tot=tot+marks
#         print("-"*50)
#         print("total marks--------->{}".format(tot))
#         print("-" * 50)
#     #main program
# fdisp_kvl(100,"prash","x",ss=50,edc=20,vlisi=20)

#type 2
def find_tl(id,sname,deg,city="hyd",**sub):
    print("-"*50)
    print("studentid----->{}".format(id))
    print("studentname----->{}".format(sname))
    print("studentclass----->{}".format(deg))
    print("student city------->{}".format(city))
    print("*"*50)
    if len(sub)!=0:
        tot=0
        for s,m in sub.items():
            print("\tsub--->{},\tmarks---->{}".format(s,m))
            tot=tot+m
        print("-"*50)
        print("tottal marsk{}".format(tot))
        print("-"*50)
#main progran
find_tl(100,"prasha","b,tech",s=99,c=99,edc=56,dcld=56,adc=99,cs=58,city="nl")
find_tl(100,"prasha","b,tech","nl",s=99,c=99,edc=56,dcld=56,adc=99,cs=58)
find_tl(sname="pars",deg="cc",s=99,c=99,edc=56,dcld=56,adc=99,cs=58,city="nl",id=100)