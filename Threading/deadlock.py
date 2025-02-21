#write a python program on deadlock by using thread
import threading
# import time
class nov:
    def __init__(self,n):
        self.n=n
    def table(self):
        if self.n<=0:
            print("this is invalid input{}".format(self.n))
        else:
            for i in range(1,11):
                print("{},{}*{}-->{}".format(threading.current_thread().name,self.n,i,self.n*i))
                # time.sleep(1)
#main program
n=int(input("enter a number"))
t1=threading.Thread(target=nov(n).table)
t2=threading.Thread(target=nov(n).table)
t1.name="pars"
t2.name="anil"
t1.start()
t2.start()