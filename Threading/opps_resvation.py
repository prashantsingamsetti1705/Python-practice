#writre a python program using the sync thread by geanrate resvation of the seat
#import threading and time
import threading,time
class Train:
    l = threading.Lock()
    totalesat=18
    def res(self,n):
        Train.l.acquire()
        if n>Train.totalesat:
            print("{} better luck next time".format(threading.current_thread().name,n))
        else:
            Train.totalesat=Train.totalesat-n
            print("{}your {} seat is selected".format(threading.current_thread().name,n))
            print("the remaing {} seats left".format(Train.totalesat))
            if Train.totalesat==0:
                print("train is full")
        Train.l.release()
        time.sleep(1)

#creating the sub thread
t1=threading.Thread(target=Train().res,args=(6,))
t1.name="prashant"
t1.start()
print("-"*50)
t2=threading.Thread(target=Train().res,args=(2,))
t2.name="anil"
t2.start()
print("-"*50)
t3=threading.Thread(target=Train().res,args=(8,))
t3.name="subbarao"
t3.start()
print("-"*50)
t4=threading.Thread(target=Train().res,args=(8,))
t4.name="suhaisni"
t4.start()
