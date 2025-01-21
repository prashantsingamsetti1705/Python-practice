#Program for Finding Square Root of Every Element of List
#ListComprehensionEx2.py
lst=[12,4,15,8,45,-5,0,17]
print("Given List=",lst)
sqlist=[ val**0.5   for val in lst] # List Comprehension
print("---------------------------------------")
print("Given Value\t\tSquare Root")
print("---------------------------------------")
for ov,sv in zip(lst,sqlist):
    if(type(sv)!=complex):
        print("\t{}\t\t\t{}".format(ov,round(sv,2)))
    else:
        print("\t{}\t\t\t{}".format(ov,sv))

print("---------------------------------------")

#Program for Finding List of +Ve and -Ve Values from List of Values
lst=[10,-12,30,-40,-50,13,56,-23,-78,90,0,16,-17,66,-55,10]
print("Given List of Elements=",lst)
pslist=[ val   for  val in lst   if val>0  ] # List Comprehension
print("+Ve List=",pslist)
nglist=[val for val in lst if val<0] # List Comprehension
print("-Ve List=",nglist)
