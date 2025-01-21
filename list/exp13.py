# Python | Count occurrences of an element in a list
#logic-1
lst=[10,10,20,40,66,45]
print(lst.count(10))
#logic-2
n=int(input("enter how many numbers u want: "))
if n<=0:
    print("{} is a inavalid number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter a number in a list:".format(i)))
        lst.append(val)
    else:
        print(lst)
        print("the no of count{} is element ".format(lst.count(10)))