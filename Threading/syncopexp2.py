#write a python program on sync
import threading,time
class Table:
    @classmethod
    def getlock(cls):
        cls.l=threading.Lock()
    def __init__(self,n):
        self.n=n
    def table(self):
        Table.l.acquire()
        if self.n<=0:
            print("{} is invalid input".format(self.n))
        else:
            for val in range(1,11):
                print("{} the name of thread table of {}*{}--->{}".format(threading.current_thread().name,self.n,val,self.n*val))
                time.sleep(1)
            Table.l.release()
#main program
Table.getlock()
nov=int(input("enter the mul table value"))
t1=threading.Thread(target=Table(nov).table)
t1.name="pras"
t2=threading.Thread(target=Table(nov).table)
t2.name="anil"
t1.start()
t2.start()