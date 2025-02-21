#write a python program to n natural +ve number by using thread
import threading
def nat(n):
    if n<=0:
        print("invalid input please try again")
    else:
        for i in range(1,n+1):
            print("the {}value of the i name thread is{}".format(i,threading.current_thread().name))




