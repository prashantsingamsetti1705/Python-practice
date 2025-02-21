# write a python program of eaxmple of the thread and theradcount
#frist we have to import thread
import threading
tname=threading.current_thread().name#we acn find the name of thread
print("the deafault thread name is{}".format(tname))
print("the deafault thread count is {}".format(threading.active_count()))
