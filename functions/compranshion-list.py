#Program for Finding Square of Every Element of List
#ListComprehensionEx1.py
lst=[12,4,15,8,-5,0,17]
print("Given List=",lst)
sqlist=[ val**2   for val in lst] # List Comprehension
print("---------------------------------------")
print("Given Value\t\tSquare Value")
print("---------------------------------------")
for ov,sv in zip(lst,sqlist):
    if(type(sv)!=complex):
        print("\t{}\t\t\t{}".format(ov,round(sv,2)))
    else:
        print("\t{}\t\t\t{}".format(ov,sv))
print("---------------------------------------")

