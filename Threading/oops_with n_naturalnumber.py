#by using the constructer
import threading
class Nat:
    def __init__(self,n):
        self.n=n
    def nat(self):
        if self.n<=0:
            print("invalid input please try again")
        else:
            for i in range(1,self.n+1):
                print("the {}value of the i name thread is{}".format(i,threading.current_thread().name))

#mainn program threading
nov=int(input("enter a number"))
t1=threading.Thread(target=Nat(nov).nat)
t1.name="prash"
t1.start()
t1.join()

#Program for generating 1 to N after each and every Second where  n is +ve by using threads
#NumberGenOOPsEx2.py
import threading,time
class GenNum:
	def __init__(self,n):
		self.n=n
	def generate(self):
		if(self.n<=0):
			print("{}--->{} Invalid Input".format(threading.current_thread().name,self.n))
		else:
			print("-"*50)
			print("Numbers within:{}".format(self.n))
			print("-"*50)
			for i in range(1,self.n+1):
				print("{}-Value of i={}".format(threading.current_thread().name,i))
				time.sleep(0.25)
			print("-"*50)

#Main Program
nov=int(input("Enter How Many Numbers u want to generate:"))
t1=threading.Thread(target=GenNum(nov).generate)
t1.name="KVR"
t1.start()