#write a python program of main thread and find out the thread anme
#frist we have to import threading
import threading
def hello(sname):#using the function and parameters
    print("the  sname is{}".format(sname))
    print("the count thread is{}".format(threading.active_count()))
#main program
#calling function
print("the program is starting")
print("the default thread is{}".format(threading.current_thread().name))
hello("prashant")
print("the program is ending")
print("the default thread is{}".format(threading.current_thread().name))
