#write a python program on even number and odd number by using the threading
import threading,time
def even(n):
    if n<=0:
        print("this is invalid input")
    else:
        for i in range(1,n+1,2):
            print("{} the value is{}".format(threading.current_thread().name,i))
            time.sleep(1)
def odd(n):
    if n<=0:
        print("this is invalid input")
    else:
        for i in range(2,n+1,2):
            print("{} the value is{}".format(threading.current_thread().name,i))
            time.sleep(1)
#main program
t1=threading.Thread(target=even,args=(5,))
t2=threading.Thread(target=odd,args=(5,))
t1.start()
t2.start()


