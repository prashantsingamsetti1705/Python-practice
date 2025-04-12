#write a python pgogram for demonstarting the nedd of coluser
#firts sample examples
#InnerOuterFunsEx1.py
def functionA():
   print ("Outer function")
   def functionB():
      print ("Inner function")
   functionB()

#Main Program
functionA()

#InnerOuterFunsEx1.py
def functionA():
   print ("Outer function")
   def functionB():
      print ("Inner function")
   return functionB

#Main Program
funb=functionA()
funb()

#innerouter function ex3.py
def funA(name):
    print("iam outer function")
    def funb():
        print("iam inner function")
        print("hi {}".format(name))
    funb()
#main program
funA("python")

def fun1(x):
    def fun2(y):
        z=x+y
        return z
    return fun2
#main program
kvr=fun1(1)
print("the value of the xyz is:",kvr(5))

def cal():#outer function
    num=0#local var
    def opera():#inner function
        nonlocal num
        num=num+1
        return num
    return opera
#main program
op=cal()
print("the first time of the op is=",op())
print("the sec time of the op is=",op())
print("the third time of the op is=",op())
#program for demonstarting  the need of closures
#closure exa3
def greet(sub):
    sname="rosum"
    print("outer function result:",sname)
    lf=lambda val:"hi {},{},{}, good morning".format(sname,sub,val)
    print("iam from the outer function")
    return lf
w=greet("python")
print(w("travis"))
print(w("hunter"))

