#Program for finding Biggest  of List of Values
#ReduceEx2.py
import functools
lst=list(map(float,input("Enter List of Values Separated by Space:").split()))
print("Given Values:")
print(lst)
#Logic for Finding Max  and min from List of Values
bv=functools.reduce(lambda x,y: x if x>y else y, lst)
sv=functools.reduce(lambda x,y: x if x<y else y, lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))

#Program for finding Biggest  of List of Values
#Reduce
import functools
def bigv(k,v):
	if(k>v):
		return k
	else:
		return v

def smallv(k,v):
	if(k<v):
		return k
	else:
		return v

lst=list(map(float,input("Enter List of Values Separated by Space:").split()))
print("Given Values:")
print(lst)
#Logic for Finding Max  and min from List of Values
bv=functools.reduce(bigv, lst)
sv=functools.reduce(smallv, lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))

#Program for finding Biggest  of List of Values
#ReduceEx5.py
import functools
def bigv(k,v):
	return (k if k>v else v)

def smallv(k,v):
	return (k if k<v else v)

lst=list(map(float,input("Enter List of Values Separated by Space:").split()))
print("Given Values:")
print(lst)
#Logic for Finding Max  and min from List of Values
bv=functools.reduce(bigv, lst)
sv=functools.reduce(smallv, lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))