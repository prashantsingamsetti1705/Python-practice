#now we are woking the subthread
#first we have to import threading
import threading
def sqaure(n):
    print("the square of the value is{}".format(n**2))
def cube(n):
    print("the cube of the value is{}".format(n**3))
#creating the sub objects
t1=threading.Thread(target=sqaure,arg=(5,))
t2=threading.Thread(target=cube,args=(5,))
#the name of sub threads
print("before changing the sub names")
print("the name of the thread",t1.name)
print("the name of the thread",t2.name)
print("-"*100)
t1.name="hello"
t2.name="hello2"
print("after changing the sub names")
print("the name of the thread",t1.name)
print("the name of the thread",t2.name)
print("-"*100)
