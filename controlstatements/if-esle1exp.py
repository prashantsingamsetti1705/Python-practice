#write python program to display the  given number  into digits
#by using simple if & and if else & if elif else
# d=float(input("enter a  number:"))
# if d==0:
#     print("{} is a zero".format(d))
# if d==1:
#     print("{} is One".format(d))
# if d==2:
#     print("{} is two".format(d))
# if d==3:
#     print("{} is three".format(d))
# if d==4:
#     print("{} is Four".format(d))
# if d==5:
#     print("{} is Five".format(d))
# if d==6:
#     print("{} is Six".format(d))
# if d==7:
#     print("{} is Seven".format(d))
# if d==8:
#     print("{} is Eight".format(d))
# if d==9:
#     print("{} is Nine".format(d))
# if d  in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#     print("{} is -ve digit ".format(d))
# if d>9:
#     print("{} is +ve number".format(d))
# if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#     print("{} is -ve number".format(d))
#
# d=float(input("enter a  number:"))
# if d==0:
#     print("{} is a zero".format(d))
# else:
#     if d==1:
#         print("{} is One".format(d))
#     else:
#         if d==2:
#             print("{} is two".format(d))
#         else:
#             if d==3:
#                 print("{} is three".format(d))
#             else:
#                 if d==4:
#                     print("{} is Four".format(d))
#                 else:
#                     if d==5:
#                         print("{} is Five".format(d))
#                     else:
#                         if d==6:
#                             print("{} is Six".format(d))
#                         else:
#                             if d==7:
#                                 print("{} is Seven".format(d))
#                             else:
#                                 if d==8:
#                                     print("{} is Eight".format(d))
#                                 else:
#                                     if d==9:
#                                         print("{} is Nine".format(d))
#                                     else:
#                                         if d  in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#                                             print("{} is -ve digit ".format(d))
#                                         else:
#                                             if d>9:
#                                                 print("{} is +ve number".format(d))
#                                             else:
#                                                 if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#                                                     print("{} is -ve number".format(d))

d1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"Nine",-1:"-one",-2:"-two",-3:"-three",-4:"-four",-5:"-five",-6:"-six",-7:"-seven",-8:"-eight",-9:"-Nine",}
dig=float(input("enter a digit:"))
print("{}is{}".format(dig,d1 if d1.get(dig)!=None else "+ve number" if dig>9 else "-ve number"))
