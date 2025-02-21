#now we are woking the subthread
#first we have to import threading
import threading
def sqaure(n):
    print("the square of the value is{}".format(n**2))
def cube(n):
    print("the cube of the value is{}".format(n**3))
#creating the sub objects
t1=threading.Thread(target=sqaure,args=(5,))
t2=threading.Thread(target=cube,args=(5,))
#the name of sub threads
print("program starting")
print("the thread is {}".format(threading.current_thread().name))
print("the thread is alive",t1.is_alive())
print("the thread is alive",t2.is_alive())
print("the name of the thread",t1.name)
print("the name of the thread",t2.name)
print("-"*100)
t1.start()
print("the thread is alive",t1.is_alive())
t2.start()
print("the thread is alive",t2.is_alive())
print("ending program starting")
print("the thread is {}".format(threading.current_thread().name))
print("-"*100)