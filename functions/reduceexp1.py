#Program for finding Sum of List of Vaalues
#ReduceEx1.py
import functools
lst=list(map(float,input("Enter List of Values Separated by Space:").split()))
print("Given Values:")
print(lst)
#find sum of list of Values
res=functools.reduce(lambda k,v: k+v, lst)
print("Sum({})={}".format(lst,res))

#Program for finding Sum of List of Vaalues
#model2
import functools
def sumop(k,v):
	return (k+v)

#Main Program
lst=list(map(float,input("Enter List of Values Separated by Space:").split()))
print("Given Values:")
print(lst)
#find sum of list of Values
res=functools.reduce(sumop, lst)
print("Sum({})={}".format(lst,res))