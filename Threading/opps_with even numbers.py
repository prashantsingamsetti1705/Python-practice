
#now by using the opps concept

import threading,time
class Val:
    def even(self,n):#instance method
        if n<=0:
            print("this is invalid input{}",n)
        else:
            for i in range(1,n+1,2):
                print("{} the value is{}".format(threading.current_thread().name,i))
                time.sleep(1)
    def odd(self,n):
        if n<=0:
            print("this is invalid input{}",n)
        else:
            for i in range(2,n+1,2):
                print("{} the value is{}".format(threading.current_thread().name,i))
                time.sleep(1)
#main program
#creating a sperate thread for displaying the even numbers
t1=threading.Thread(target=Val().even,args=(5,))
#creating a sperate thread for displaying the odd numbers
t2=threading.Thread(target=Val().odd,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
#now we are using the
#parameterizedconsturcter
#now by using the opps concept

import threading,time
class nov:
    def __init__(self,n):
        self.n=n
    def even(self):
        if self.n<=0:
            print("this is invalid input{}".format(self.n))
        else:
            for i in range(2,self.n+1,2):
                print("",threading.current_thread().name,i)
                time.sleep(1)
    def odd(self):
        if self.n<=0:
            print("this is invalid input{}".format(self.n))
        else:
            for i in range(1,self.n+1,2):
                print("", threading.current_thread().name, i)
                time.sleep(1)
#main program
n=int(input("enter a number"))
t1=threading.Thread(target=nov(n).even)
t2=threading.Thread(target=nov(n).odd)
t1.start()
t2.start()
