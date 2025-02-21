import threading
def hi():
    print("the thread name is :",threading.current_thread().name)
def welcome():
    print("the thread name is :",threading.current_thread().name)
def hello():
    print("the thread name is :",threading.current_thread().name)
t1=threading.Thread(target=hi)
t2=threading.Thread(target=welcome)
t3=threading.Thread(target=hello)
print("the program starting")
print("the default program is{}".format(threading.current_thread().name))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("the program ending")
print("the default program is{}".format(threading.current_thread().name))