import threading,time
def res(n):
    l.acquire()
    global vaccm
    if n>vaccm:
        print("{} better luck next time".format(threading.current_thread().name,n))
    else:
        vaccm=vaccm-n
        print("{}your {} check is passed collect the money".format(threading.current_thread().name,n))
        print("the remaining {} money left".format(vaccm))
        if vaccm==0:
            print("your check is bounced")
    l.release()
    time.sleep(1)
#
vaccm=160000
l=threading.Lock()
#creating the sub thread
t1=threading.Thread(target=res,args=(60000,))
t1.name="prashant"
t1.start()
print("-"*50)
t2=threading.Thread(target=res,args=(20000,))
t2.name="anil"
t2.start()
print("-"*50)
t3=threading.Thread(target=res,args=(40000,))
t3.name="subbarao"
t3.start()
print("-"*50)
t4=threading.Thread(target=res,args=(80000,))
t4.name="suhaisni"
t4.start()