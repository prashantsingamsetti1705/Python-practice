#logic-3 a=a+b,b=a-b,a=a-b
a,b=int(input("enter value of a:")),int(input("enter value of b:"))
print("*"*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("*"*50)
#swapping logic
a=a+b
b=a-b
a=a-b
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))
#logic-4 a=a*b,b=a//b,a=a//b
a,b=int(input("enter value of a:")),int(input("enter value of b:"))
print("*"*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("*"*50)
#swapping logic
a=a*b
b=a//b
a=a//b
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))

#logic-5 a=a^b,b=a^b,a=a^b
a,b=int(input("enter value of a:")),int(input("enter value of b:"))
print("*"*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("*"*50)
#swapping logic
a=a^b
b=a^b
a=a^b
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))
