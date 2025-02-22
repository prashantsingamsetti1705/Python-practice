#writre a python program using the sync thread by geanrate resvation of the seat
#import threading and time
import threading,time
def res(n):
    l.acquire()
    global totalesat
    if n>totalesat:
        print("{} better luck next time".format(threading.current_thread().name,n))
    else:
        totalesat=totalesat-n
        print("{}your {} seat is selected".format(threading.current_thread().name,n))
        print("the remaing {} seats left".format(totalesat))
        if totalesat==0:
            print("train is full")
    l.release()
    time.sleep(1)
#
totalesat=16
l=threading.Lock()
#creating the sub thread
t1=threading.Thread(target=res,args=(6,))
t1.name="prashant"
t1.start()
print("-"*50)
t2=threading.Thread(target=res,args=(2,))
t2.name="anil"
t2.start()
print("-"*50)
t3=threading.Thread(target=res,args=(8,))
t3.name="subbarao"
t3.start()
print("-"*50)
t4=threading.Thread(target=res,args=(8,))
t4.name="suhaisni"
t4.start()