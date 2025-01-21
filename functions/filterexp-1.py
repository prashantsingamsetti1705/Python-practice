#write apython program which print only postive elements
#filters function using four different methods
def pos(val):
    if val>0:
        return True
    else:
        return False
def neg(val):
    if val<0:
        return True
    else:
        return False
#main program
lst=[10,20,30,-9,12,13]
obj1=filter(pos,lst)
obj2=filter(neg,lst)
lst1=list(obj1)
lst2=list(obj2)
print(lst)
print(lst1)
print(lst2)

#reading values by key bord
#write a python program which print only positive elements
def pos(val):
    if val>0:
        return True
    else:
        return False
def neg(val):
    if val<0:
        return True
    else:
        return False
#main program
lst=[float(val) for val in input().split()]
obj1=filter(pos,lst)
obj2=filter(neg,lst)
lst1=list(obj1)
lst2=list(obj2)
print(lst)
print(lst1)
print(lst2)

#using the the
ps=lambda val:val>0
ng=lambda val:val<0
#main program
lst=[float(val) for val in input().split()]
lst1=list(filter(ps,lst))
lst2=list(filter(ng,lst))
print("given numbers")
print(lst1)
print(lst2)
#
lstv=[float(val) for val in input().split()]
lst1=list(filter(lambda val1: val1>0,lstv))
lst2=list(filter(lambda val2: val2<0,lstv))
print("given numbers")
print(lst1)
print(lst2)