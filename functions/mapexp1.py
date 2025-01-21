#writea a python program which used to update the old sal to new sal without using list comprehension
def hike(sal):
    return sal+sal*50/100
#main program
old_sal=list(map(float,input("enter the list of values").split()))
#given sal
new_sal=list(map(hike,old_sal))
print("\told_sal\t\tnew_sal")
print("-"*50)
for osl,nsl in zip(old_sal,new_sal):
    print("\t{}\t\t{}".format(osl,nsl))
#wrtoe the program using the anonumos function
odsal=list(map(float,input("enter the list of values").split()))
#given sal
newsal=list(map(lambda sal:sal+sal*50/100,odsal))
print("\told_sal\t\tnew_sal")
print("-"*50)
for osl,nsl in zip(odsal,newsal):
    print("\t{}\t\t{}".format(osl,nsl))
#wrtoe the program using the anonumos function