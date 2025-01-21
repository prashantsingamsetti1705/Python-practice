#epx1 program for swapping the elementsin multeline statements
#logic-1 a,b=b,a
a,b=input("enter value of a:"),input("enter value of b:")
print("*"*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("*"*50)
a,b=b,a
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))

#logic-2  t=a,a=b,t=b
a,b=input("enter value of a:"),input("enter value of b:")
print("*"*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("*"*50)
t=a
a=b
b=t
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))




