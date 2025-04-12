#write a python program on the simple example on the iterators
s=["appele","hii","anil"]
myot=iter(s)
print(next(myot))
print(next(myot))
print(next(myot))

#program on for demon starting the iterators with traditional iterable
#
import sys
x=[100,"roosum",34.6,"python"]#list type
print("-"*50)
print("content of the x=,x")
print("type of x",type(x))
print("-"*50)
#converting the object type into iterator type
#varname=iter(itarable obj)
xit=iter(x)
print("contet of the xiter",xit)
print("type of the xiter=",type(xit))
print("-"*50)
print("content of the itterator by usimg the next()")
try:
    print(next(xit))
    print(next(xit))
    print(next(xit))
    print(next(xit))
    print(next(xit))
except StopIteration:
    print("-"*50)
    sys.exit()