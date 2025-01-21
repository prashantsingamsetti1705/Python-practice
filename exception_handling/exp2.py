#write a python program using the exception handling-------- keywords gen the program
try:
    print("*"*50)
    s1=input("enter the a value of s1:")
    s2=input("enter the the value of s2")
    a=int(s1)
    b=int(s2)
    c=a/b
    print("the value of s1=",s1)
    print("the value of s2=",s2)
except (ZeroDivisionError,ValueError):
    print("dont enter the value the zero u will get the zero division error")
    print("dont the the alphanum u will get the error---value error")
else:
    print("----------iam from else block to di splay the result")
    print(a)
    print(b)
    print(c)
finally:
    print("--------------")
    print("iam from the finally block")

