# write a program to perform the relation operators
#there are 6 operators >,<,==,!=,>=,<=
#program
a,b=float(input("enter value of a:")),float(input("enter value of b:"))
print("*"*50)
print("{}>{} ={}".format(a,b,a>b))
print("{}< ={}".format(a,b,a<b))
print("*"*50)
print("{}=={},={}".format(a,b,a==b))
print("{}!={},={}".format(a,b,a!=b))
print("*"*50)
print("{} >= {},={}".format(a,b,a>=b))
print("{}<={},={}".format(a,b,a<=b))
print("*"*50)