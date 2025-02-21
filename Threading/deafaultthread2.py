#write a pytho program on thread concept
import threading
def hi():
    print("hi executed by thread name is{}".format(threading.current_thread().name))
def wellcome():
    print("wellcome executed by thread name  is{}".format(threading.current_thread().name))
def hello():
    print("hello executed by thread name is{}".format(threading.current_thread().name))
#main program
print("-"*50)
print("program execution starting")
print("default name of the current thread-->{}".format(threading.current_thread().name))
hi()
wellcome()
hello()
print("-"*50)
print("program execution ending")
print("default name of the current thread-->{}".format(threading.current_thread().name))
#using the class
import threading
class Thread:#instane method
    def hi(self):
        print("hi executed by thread name is{}".format(threading.current_thread().name))
    def wellcome(self):
        print("wellcome executed by thread name  is{}".format(threading.current_thread().name))
    def hello(self):
        print("hello executed by thread name is{}".format(threading.current_thread().name))
#main program
print("-"*50)
print("program execution starting")
print("default name of the current thread-->{}".format(threading.current_thread().name))
co2=Thread()
co2.hi()
co2.wellcome()
co2.hello()
print("-"*50)
print("program execution ending")
print("default name of the current thread-->{}".format(threading.current_thread().name))