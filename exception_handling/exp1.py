# #write a program using the exception handling by using the from---1
try:
    print("*"*50)
    s1=input("enter the value of s1:")
    s2=input("enter the value of s2:")
    a=int(s1)#value error
    b=int(s2)#value error
    c=a/b
except ZeroDivisionError:
    print("dont enter the 0 u will get the error")
except ValueError:
    print("dont enter the alphanum,str u will get the error")
else:
    print("*"*50)
    print("\ta=",a)
    print("\tb=",b)
    print("div=",c)
finally:
    print("iam from the finally block")
