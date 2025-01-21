#write apython proram which is used sum of list1,lst2 in lst3
# lst1=list(map(float,input("enter the list of values").split()))
# lst2=list(map(float,input("enter the list of values").split()))
# if len(lst1)>len(lst2):
#     for i in range(len(lst1)-len(lst2)):
#         lst2.append(0)
# elif len(lst2)>len(lst1):
#     for i in range(len(lst2)-len(lst1)):
#         lst1.append(0)
# lst3=list(map(lambda x,y:x+y,lst1,lst2))
# print("-"*50)
# print("\tList1\t\tList2\t\tSumList")
# print("-"*50)
# for val1,val2,val3 in zip(lst1,lst2,lst3):
#     print("\t{}\t\t{}\t\t\t{}".format(val1,val2,val3))
#write a python program which used to add the book name and the author
bookname=list(map(str,input("enter the book names with sapce").split()))
aouthor=list(map(str,input("enter the book aouthors").split()))
if len(bookname)>len(aouthor):
    for i in range(len(bookname)-len(aouthor)):
        aouthor.append("unknown")
elif len(aouthor)>len(bookname):
    for i in range(len(aouthor)-len(bookname)):
        bookname.append("unknown")
lst3=list(map(lambda x,y:x+y,bookname,aouthor))
print("-"*50)
print("\tbookname\t\taouthor\t\tbooknameby aouthr")
print("-"*50)
for val1,val2,val3 in zip(bookname,aouthor,lst3):
    print("\t{}\t\t{}\t\t\t{}".format(val1,val2,val3))

