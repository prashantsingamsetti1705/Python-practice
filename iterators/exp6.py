#write a python program on the iterators in python by converting the tuple in iterators
x={"python":100,"roosum":34.6,"anil":25}
print("-"*50)
print("content of the x=,x")
print("type of x",type(x))#dict
print("-"*50)
#converting the object type into iterator type
#varname=iter(itarable obj)
xit=iter(x)
print("contet of the xiter",xit)
print("type of the xiter=",type(xit))
print("-"*50)
print("content of the itterator by usimg the next()")
while True:
    try:
        k=next(xit)
        print("the value the k is {}".format(k,x.get(k)))
    except StopIteration:
        print("-"*50)
        break