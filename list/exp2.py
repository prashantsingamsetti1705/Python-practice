# Python | Ways to check if element exists in list
# logic -1
lst=[10,20,30,40]
if 30 in lst:
    print("this a existing list{}".format(lst))
else:
    print("this is not a existing list{}".format(lst))
# logic -2
lst=[10,20,30,40]
if lst.count(30):
    print("this is a existing list".format(lst))
else:
    print("this is a not a existing list ".format(lst))
#logic-3
lst=[10,20,30,40]
a=30
el=False
for i in lst:
   if i==a:
       el=True
       break
if el :
    print("{} is my list ".format(a))
else:
    print("{} is  not my list".format(a))
