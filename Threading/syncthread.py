#write a python program on deadlock by using thread
import threading
import time
def table(n):
    l.acquire()
    if n<=0:
        print("this is invalid input{}".format(n))
    else:
        for i in range(1,11):
            print("{},{}*{}-->{}".format(threading.current_thread().name,n,i,n*i))
            time.sleep(1)
    l.release()
#main program
l=threading.Lock()
n=int(input("enter a number"))
t1=threading.Thread(target=table,args=(n,))
t2=threading.Thread(target=table,args=(n,))
t1.name="pars"
t2.name="anil"
t1.start()
t2.start()

