#deafult threading using the example
import threading,time
def sqr(lst):
    for val in lst:
        print("the sqr of the value {} and name of the thread{}".format(val**3,threading.current_thread().name))
        time.sleep(1)
def cube(lst):
    for val in lst:
        print("the cube of the value {} and name of the thread{}".format(val**3,threading.current_thread().name))
        time.sleep(1)
#mian program
bt=time.time()#before excu
lst=[10,20,30,40,5]
print("the program starting")
print("the default program is{}".format(threading.current_thread().name))
print("-"*50)
sqr(lst)
print("-"*50)
cube(lst)
print("the program ending")
print("the default program is{}".format(threading.current_thread().name))
et=time.time()#afterecxuting
print("the time taken is {}".format(round(et-bt)))
