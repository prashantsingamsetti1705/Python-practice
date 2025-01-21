#Program for getting Line of Text from List of Words
#ReduceEx6.py
import functools
#Main Program
lst=list(map(str,input("Enter List of Words Separated by Comma:").split(",")))
print("-------------------------------")
print("Given Words:")
print(lst)
print("-------------------------------")
line=functools.reduce(lambda k,v:k+" "+v,lst)
print("Line of Text:")
print(line)

#Program for getting Line of Text from List of Words
#Reduce
import functools
def kvrjoin(k,v):
	return (k+" "+v)
#Main Program
lst=list(map(str,input("Enter List of Words Separated by Comma:").split(",")))
print("-------------------------------")
print("Given Words:")
print(lst)
print("-------------------------------")
line=functools.reduce(kvrjoin,lst)
print("Line of Text:")
print(line)