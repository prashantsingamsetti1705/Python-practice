import threading,time
class Train:
    @ classmethod
    def com(cls):
        cls.l= threading.Lock()
        cls.totalesat=18
    def __init__(self,n):
        self.n=n
    def res(self):
        Train.l.acquire()
        if self.n>Train.totalesat:
            print("{} better luck next time".format(threading.current_thread().name,self.n))
        else:
            Train.totalesat=Train.totalesat-self.n
            print("{}your {} seat is selected".format(threading.current_thread().name,self.n))
            print("the remaing {} seats left".format(Train.totalesat))
            if Train.totalesat==0:
                print("train is full")
            time.sleep(1)
        Train.l.release()

#creating the sub thread
Train.com()
t1=threading.Thread(target=Train(6).res)
t1.name="prashant"
#disapcting it
t1.start()
t2=threading.Thread(target=Train(6).res)
t2.name="anil"
t2.start()
t3=threading.Thread(target=Train(8).res)
t3.name="subbarao"
t3.start()
t4=threading.Thread(target=Train(6).res)
t4.name="suhaisni"
t4.start()