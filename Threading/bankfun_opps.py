import threading,time
class Bank:
    @classmethod
    def com(cls):#class level method
        cls.vaccm = 160000
        cls.l = threading.Lock()
    def __init__(self,n):#construcot method
        self.n=n
    def res(self):
        Bank.l.acquire()
        if self.n>Bank.vaccm:
            print("{} better luck next time".format(threading.current_thread().name,self.n))
            time.sleep(3)
        else:
            Bank.vaccm=Bank.vaccm-self.n
            print("{}your {} check is passed collect the money".format(threading.current_thread().name,self.n))
            print("the remaining {} money left".format(Bank.vaccm))
            if Bank.vaccm==0:
                print("your check is bounced")
                time.sleep(3)
        Bank.l.release()
#
#creating the sub thread
#dispatching the values
Bank.com()
t1=threading.Thread(target=Bank(20000).res)
t1.name="prashant"
t1.start()
t2=threading.Thread(target=Bank(20000).res)
t2.name="anil"
t2.start()
t3=threading.Thread(target=Bank(40000).res)
t3.name="subbarao"
t3.start()
t4=threading.Thread(target=Bank(80000).res)
t4.name="suhaisni"
t4.start()